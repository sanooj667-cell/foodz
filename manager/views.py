from django.shortcuts import render , reverse,get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as login_manager, logout as logout_manager
from customer.models import Order_items, Address, CartItem,Customer
from restaurent.models import Storecategory, Slider, Store
from manager.forms import *
from main.function import genarate_form_error


# Create your views here.

def index(request):

    instances = Order_items.objects.all()

    context = {
        "instances" : instances
    }

    return render (request,"manager/index.html", context=context)


def login(request):
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request,email=email,password = password)
        if user is not None and user.is_superuser:
            login_manager(request,user)
            return HttpResponseRedirect(reverse("manager:index"))
        else:
            message = "invalid email or password"
            context = {
                "message":message
            }
            return render(request, 'manager/login.html',context=context)
    else:
        return render(request, "manager/login.html")



# ----------------------store-----------------------------------------------------------


def store(request):

    instances = Store.objects.all()

    context = {
        "instances" : instances
    }
    
    return render(request,"manager/store.html", context=context)


def store_creat(request):
    if request.method == "POST":
        form = StoreForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:store'))
        
        else:
            messege = genarate_form_error(form)
            form = StoreForm()
            context = {
                "form" : form,
                "errors" : True,
                "message" : messege
            }
            return render(request , "manager/add_store.html", context=context)
    else:
        form = StoreForm()

        context= {
            "form" : form
        }
        
        return render(request , "manager/add_store.html", context=context)
    







def store_update(request,id):

    instance = get_object_or_404(Store, id=id)

    if request.method == "POST":
        form = StoreForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("manager:store"))
            
        else:
            messege =  genarate_form_error(form)
            form = StoreForm()

            context = {
                "messege" : messege,
                "errors" : True,
                "messege" : messege,
            }
            return render(request , "manager/add_store.html", context=context)




    else:
        form = StoreForm(instance=instance)
        context = {
            "form" : form
        }  

        return render(request , "manager/add_store.html", context=context)    
    












# ----------------------store category-----------------------------------------------------------


def store_category(request):

    instances = Storecategory.objects.all()

    context = {
        "instances" : instances
    }
    
    return render(request,"manager/store-categories.html", context=context)


def store_category_creat(request):
    if request.method == "POST":
        form = StoreCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:store_category'))
        
        else:
            messege = genarate_form_error(form)
            form = StoreCategoryForm()
            context = {
                "form" : form,
                "errors" : True,
                "message" : messege
            }
            return render(request , "manager/add-store-categories.html", context=context)
    else:
        form = StoreCategoryForm()

        context= {
            "form" : form
        }
        
        return render(request , "manager/add-store-categories.html", context=context)
    

def store_delete(request, id):
    instance = get_object_or_404(Store, id=id)
    instance.delete()

    return HttpResponseRedirect(reverse('manager:store'))
    




    

def store_category_update(request,id):

    instance = get_object_or_404(Storecategory, id=id)

    if request.method == "POST":
        form = StoreCategoryForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("manager:store_category"))
            
        else:
            messege =  genarate_form_error(form)
            form = StoreCategoryForm()

            context = {
                "messege" : messege,
                "errors" : True,
                "messege" : messege,
            }
            return render(request , "manager/add-store-categories.html", context=context)




    else:
        form = StoreCategoryForm(instance=instance)
        context = {
            "form" : form
        }  

        return render(request , "manager/add-store-categories.html", context=context)





def store_category_delete(request, id):
    instance = get_object_or_404(Storecategory, id=id)
    instance.delete()

    return HttpResponseRedirect(reverse('manager:store_category'))
    

    








def slider(request):

    instances =Slider.objects.all()

    context = {
        "instances" : instances
    }
    
    return render(request,"manager/slider.html", context=context)










#  ------------------------ product--------------------------------------------

def foodcategory(request):

    instances = FoodCatagory.objects.all()

    context = {
        "instances" : instances
        }
    
    return render(request, "manager/food_category.html", context=context)



def foodcategory_creat(request):
    if request.method == "POST":
        form = FoodCtegoryForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:foodcategory'))
        
        else:
            messege = genarate_form_error(form)
            form = FoodCtegoryForm()
            context = {
                "form" : form,
                "errors" : True,
                "message" : messege
            }
            return render(request , "manager/add _foodcategory.html", context=context)
    else:
        form = FoodCtegoryForm()

        context= {
            "form" : form
        }
        
        return render(request , "manager/add _foodcategory.html", context=context)
    



def foodcategory_update(request,id):

    instance = get_object_or_404(FoodCatagory, id=id)

    if request.method == "POST":
        form = FoodCtegoryForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("manager:foodcategory"))
            
        else:
            messege =  genarate_form_error(form)
            form = FoodCtegoryForm()

            context = {
                "messege" : messege,
                "errors" : True,
                "messege" : messege,
            }
            return render(request , "manager/add _foodcategory.html", context=context)


    else:
        form = FoodCtegoryForm(instance=instance)
        context = {
            "form" : form
        }  

        return render(request , "manager/add _foodcategory.html", context=context)
    


def foodcategory_delete(request, id):
    instance = get_object_or_404(FoodCatagory, id=id)
    instance.delete()

    return HttpResponseRedirect(reverse("manager:foodcategory"))
    















def fooditems(request):

    instances = FoodItems.objects.all()

    context = {
        "instances" : instances 
    }
    
    return render(request, "manager/food_item.html", context=context)


def fooditems_creat(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('manager:fooditems'))
        else:
            messege = genarate_form_error(form)
            form = FoodItemForm()
            context = {
                "form" : form,
                "errors" : True,
                "messege" : messege,
            }
            return render(request, "manager/add_fooditem.html", context=context)
        
    else:
        form = FoodItemForm()
        context = {
            "form" : form
        }

        return render(request, "manager/add_fooditem.html", context=context)
    

def fooditem_update(request, id):

    instance = get_object_or_404(FoodItems, id=id)    

    if request.method == "POST":
        form = FoodItemForm(request.POST,request.FILES,instance=instance)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("manager:fooditems"))
        else:
            message = genarate_form_error(form)
            form = FoodItemForm()

            context = {
                "form" : form,
                "errors" : True,
                "message" : message,
            }
            return render(request, "manager/add_fooditem.html" , context=context)

    else:
        form = FoodItemForm(instance=instance)
        context = {
            "form" :form
        }
        return render(request, "manager/add_fooditem.html" , context=context)



def fooditem_delete(request, id):
    instance = get_object_or_404(FoodItems,id=id)
    instance.delete()
    
    return HttpResponseRedirect(reverse("manager:fooditems"))










def address(request):

    instances = Address .objects.all()

    context = {
        "instances" : instances 
    }
    
    return render(request, "manager/address.html", context=context)


    

def delete_address(request, id):
    instance = get_object_or_404(Address, id=id)
    instance.delete()

    return HttpResponseRedirect(reverse("manager:address"))







def cart(request):
    instance = CartItem.objects.all()

    context = {
        "instances" : instance
    }

    return render(request, "manager/cart.html", context=context)



def delete_cart(request, id):
    instance = get_object_or_404(CartItem,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse("manager:cart"))







def order(request):
    instance = Order_items.objects.all()

    context = {
        "instances" : instance
    }

    return render(request, "manager/order.html", context=context)

def delete_order(request, id):
    instance = get_object_or_404(Order_items,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse("manager:order"))






def custamer(request):
    instance = Customer.objects.all()

    context = {
        "instances" : instance
    }

    return render(request, "manager/custamer.html", context=context)



def delete_custamer(request, id):
    instance = get_object_or_404(Customer,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse("manager:custamer"))





