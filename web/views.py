from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout   
from django.contrib.auth.decorators import login_required    

from users.models import User
from customer.models import Customer
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
 


    context = {
         "store" :single_restaurent,
         "food_categorys" :food_category,
         "food_items" :food_items,

      }


    return render(request, 'web/single_restaurent.html',context=context)





            