from django.shortcuts import render , reverse,get_object_or_404
from django.http.response import HttpResponseRedirect
from customer.models import Order_items
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
    



