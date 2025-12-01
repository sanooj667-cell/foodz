from django.shortcuts import render, reverse ,redirect
from django.http import HttpResponseRedirect
from django.db.models import Sum

from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout   
from django.contrib.auth.decorators import login_required    

from users.models import User
from customer.models import Customer,CartItem, Address, Bill, Order ,Order_items
from restaurent.models import Store, Slider ,Storecategory,FoodCatagory,FoodItems



@login_required(login_url='/login/')
def index(request):
    store_categories = Storecategory.objects.all()
    stores = Store.objects.all()
    context = {
       "store_categories" : store_categories ,
       "stores" : stores
    }
    return render(request, 'web/index.html', context=context)



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email = email, password = password)
        

        if user is not None:
           auth_login(request, user)
           return HttpResponseRedirect(reverse('web:index'))
        else:
          context ={
             'error' : True,
             'message' : 'invalid Email or password'
          } 
          return render(request, 'web/login.html', context=context)
            
    else:  
      return render(request, 'web/login.html')
        


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            context ={
            'error' : True,
            'message' : 'Email alreay exists'
            } 
            return render(request, 'web/register.html', context=context)
 
        else:
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
                is_customer = True
                
            )

            user.save()

            customer = Customer.objects.create(
                user = user
            )
            customer.save()

            return  HttpResponseRedirect(reverse('web:login'))
        
    else:
      return render(request, 'web/register.html')
    

def logout(request):
   auth_logout(request)
   return HttpResponseRedirect(reverse('web:login'))
       




@login_required(login_url='/login/')
def restaurents(request, id):
    store_categories = Storecategory.objects.all()
    stores = Store.objects.all()

    selected_category = Storecategory.objects.get(id=id)
    stores = stores.filter(catagorey = selected_category)


    context = {
       "store_categories" : store_categories ,
       "stores" : stores
    }
    return render(request, 'web/restaurents.html', context=context)






   
def single_restaurent(request, id):
    single_restaurent = Store.objects.get(id=id)
    food_category = FoodCatagory.objects.filter(store=single_restaurent)
    food_items =FoodItems.objects.filter(store=single_restaurent)

    cart = None
    count = 0 
    price = 0

    if CartItem.objects.all().exists():
        cart = CartItem.objects.all()
        count = cart.count()
        price = cart.aggregate(Sum('amount'))['amount__sum']


    product_list = []
    for item in food_items:
        cart_item = CartItem.objects.filter(item=item).first()
        if cart_item:
            quantity = cart_item.quantity
        else:
            quantity=0

        product_list.append({
            'food_item':item,
            'quantity':quantity,
            'cart' : cart_item
        })    





    context = {
         "store" :single_restaurent,
         "food_categorys" :food_category,
         "product_list" :product_list,
         "cart" : cart,
         "count" : count,
         "price" : price

      }  


    return render(request, 'web/single_restaurent.html',context=context)






def add_cart(request, id): 
    user = request.user
    customer = Customer.objects.get(user=user)
    item = FoodItems.objects.get(id = id)
    store =item.store
    amount = item.price

    existing_items = CartItem.objects.filter(customer=customer)



    if existing_items.exists():
        existing_store = existing_items.first().store

        if existing_store != store:
            existing_items.delete()


         

    CartItem.objects.create(
        customer = customer,
        store = store,
        item = item ,
        amount = amount,
        quantity =1,
    )

    return HttpResponseRedirect(reverse("web:single_restaurent", kwargs={"id":store.id}))



def cart_plus(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity = cart_item.quantity + 1
    cart_item.amount +=  cart_item.item.price
    cart_item.save()


    return HttpResponseRedirect(reverse("web:single_restaurent", kwargs={"id":cart_item.store.id}))




def cart_minies(request, id):
    user= request.user
    customer = Customer.objects.get(user = user)
    cart_item = CartItem.objects.get(id=id)

    if cart_item.quantity > 1:
        cart_item.quantity = cart_item.quantity -1
        cart_item.amount -=  cart_item.item.price
        cart_item.save()
    else:
        cart_item.delete()


    return HttpResponseRedirect(reverse("web:single_restaurent", kwargs={"id":cart_item.store.id}))







def cart(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    cart_items = CartItem.objects.filter(customer=customer)

    
    
    
    sub_totel = sum(item.amount for item in cart_items)

    offer_price = 0
    delivery_charge = 0


    totel = sub_totel - offer_price + delivery_charge
    if not Bill.objects.filter(customer=customer).exists():
        Bill.objects.create(
            customer = customer,
            sub_totel = sub_totel,
            offer_price = offer_price,
            delivary_charge = delivery_charge,
            totel = totel,
        )
    else:
        bill = Bill.objects.get(customer=customer)
        bill.sub_totel = sub_totel
        bill.totel = totel 
        bill.save()



    if not  cart_items.exists():
        Bill.objects.get(customer=customer).delete()







    store = cart_items.first().store

    selected_addres= Address.objects.filter(is_selected=True).first()


    context = {
        "cart_item":cart_items,
        "store":store,
        "selected_add":selected_addres,
        "sub_totel":sub_totel,
        "offer_price":offer_price,
        "delivery_charge":delivery_charge,
        "totel":totel,



        
    }



    return render(request, 'web/cart.html',context=context)


def cart_incriment(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity = cart_item.quantity + 1
    cart_item.amount +=  cart_item.item.price
    cart_item.save()


    return HttpResponseRedirect(reverse("web:cart"))



def cart_decriment(request, id):
    cart_item = CartItem.objects.get(id=id)

    if cart_item.quantity > 1:
        cart_item.quantity = cart_item.quantity -1
        cart_item.amount -=  cart_item.item.price
        cart_item.save()
    else:
        cart_item.delete()
        Bill.objects.get(customer = customer)


    return HttpResponseRedirect(reverse("web:cart"))
   











def address_page(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    address = Address.objects.filter(customer=customer)

    context = {
        "addres" : address,
        }


    return render(request, 'web/address.html', context=context)





def add_address(request):

    if request.method == 'POST':
        user = request.user
        custo = Customer.objects.get(user=user)
        addr = request.POST.get("address")
        app = request.POST.get("appartment")
        land = request.POST.get("landmark")
        addr_type = request.POST.get("label_as")

        Address.objects.create(
            customer= custo,
            address=addr,
            appartment=app,
            landmark=land,
            address_type=addr_type
        )

        return redirect('web:address_page')

    return render(request, 'web/add_address.html')





def delete_address(request, id):
    address = Address.objects.get(id=id)
    address.delete()


    return redirect('web:address_page')


def edit_addres(request, id ):

    address = Address.objects.get(id=id)
    context = {
        'address' : address
    }
    if request.method == 'POST':
        address.address=request.POST.get("address")
        address.appartment=request.POST.get("appartment")
        address.landmark=request.POST.get("landmark")
        address.address_type=request.POST.get("label_as")
        address.save()

        return redirect("web:address_page")
    
    return render(request, 'web/add_address.html', context=context)



def select_address(request, id):
    Address.objects.update(is_selected=False)
    selected =Address.objects.get(id=id)
    selected.is_selected = True
    selected.save()

    return redirect('web:cart')



def place_order(request):
    user = request.user
    customer = Customer.objects.get(user=user)


    cart_items = CartItem.objects.filter(customer=customer)
        
    


    address = Address.objects.get(customer=customer, is_selected =True)
    if Order.objects.filter(customer=customer).exists():
        preord = Order.objects.filter(customer=customer).first()
        order_id = f"ORD000{preord.id +1}"
    else:
        order_id = f"ORD0000"




    sub_totel = sum(item.amount for item in cart_items)
    offer_price = 0 
    delivery_charge = 0
    totel = sub_totel - offer_price + delivery_charge

    if cart_items.exists():
        order = Order.objects.create(
            customer = customer,
            address = address,
            offer_price = offer_price,
            store = cart_items.first().store,
            delivary_charge = delivery_charge,
            sub_totel= sub_totel,    
            totel = totel,
            order_id = order_id,
            status = "PENDING"
        )

        for item in cart_items:
            order_item =Order_items.objects.create(
                customer = customer,
                order = order,
                store = item.store,
                product = item.item,
                qty= item.quantity,
                amnt = item.amount,
            )


            cart_items.delete()

        return redirect("web:account")






def offer(request):


    return render(request, "web/offer.html")





def checkout(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    bill = Bill.objects.get(customer=customer)


    context = {
        "bill" : bill
    }


    return render(request, "web/checkout.html", context=context)









def account(request):
    user = request.user
    customer = Customer.objects.get(user = user)
    orders = Order.objects.filter(customer = customer)
    

   





    context ={
        "customer" : customer,
        "orders" :orders,
    }


    return render(request, "web/account.html", context=context)





def track_order(request):


    return render(request, "web/track_order.html",)










