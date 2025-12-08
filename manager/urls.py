
from django.urls import path
from manager import views

app_name ="manager"

urlpatterns = [
    path('',views.index ,name="index"),
    path('slider/',views.slider ,name="slider"),

    path('store/',views.store ,name="store"),
    path('store_creat/',views.store_creat ,name="store_creat"),
    path('store_update/<int:id>/',views.store_update ,name="store_update"),
    path('store_delete/<int:id>/',views.store_delete ,name="store_delete"),

    path('store_category/',views.store_category ,name="store_category"),
    path('store_category_creat/',views.store_category_creat ,name="store_category_creat"),
    path('store_category_update/<int:id>/',views.store_category_update ,name="store_category_update"),
    path('store_category_delete/<int:id>/',views.store_category_delete ,name="store_category_delete"),

    path('foodcategory/',views.foodcategory ,name="foodcategory"),
    path('foodcategory_creat/',views.foodcategory_creat ,name="foodcategory_creat"),
    path('foodcategory_update/<int:id>/',views.foodcategory_update ,name="foodcategory_update"),
    path('foodcategory_delete/<int:id>/',views.foodcategory_delete ,name="foodcategory_delete"),

    path('fooditems/',views.fooditems ,name="fooditems"),
    path('fooditems_creat/',views.fooditems_creat ,name="fooditems_creat"),
    path('fooditem_update/<int:id>/',views.fooditem_update ,name="fooditem_update"),
    path('fooditem_delete/<int:id>/',views.fooditem_delete ,name="fooditem_delete"),


    path('address/',views.address ,name="address"),
    path('delete_address/<int:id>/',views.delete_address ,name="delete_address"),


    path('cart/',views.cart ,name="cart"),
    path('delete_cart/<int:id>/',views.delete_cart ,name="delete_cart"),


    path('order/',views.order ,name="order"),
    path('delete_order/<int:id>/',views.delete_order ,name="delete_order"),






    
    



    



    
    

]