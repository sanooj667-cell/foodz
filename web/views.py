from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum

from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout   
from django.contrib.auth.decorators import login_required    

from users.models import User
from customer.models import Customer,CartItem
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
    store = cart_items.first().store


    context = {
        "cart_item":cart_items,
        "store":store
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


    return HttpResponseRedirect(reverse("web:cart"))
   






            