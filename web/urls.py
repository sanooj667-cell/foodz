
from django.urls import path
from web import views

app_name ="web"

urlpatterns = [
    path('',views.index ,name="index"),
    path('login/',views.login ,name="login"),
    path('register/',views.register ,name="register"),
    path('logout/',views.logout ,name="logout"),

    path('restaurents/<int:id>/',views.restaurents,name="restaurents"),
    path('single_restaurent/<int:id>/',views.single_restaurent,name="single_restaurent"),
    path('cart/',views.cart ,name="cart"),
    path('add_address/',views.add_address ,name="add_address"),
    path('address_page/',views.address_page ,name="address_page"),






    path('add_cart/<int:id>/',views.add_cart,name="add_cart"),
    path('cart_plus/<int:id>/',views.cart_plus,name="cart_plus"),
    path('cart_minies/<int:id>/',views.cart_minies,name="cart_minies"),
    path('cart_incriment/<int:id>/',views.cart_incriment,name="cart_incriment"),
    path('cart_decriment/<int:id>/',views.cart_decriment,name="cart_decriment"),
    path('add_address/',views.add_address,name="add_address"),
    path('offer/',views.offer,name="offer"),


    path('delete_address/<int:id>/',views.delete_address,name="delete_address"),
    path('edit_addres/<int:id>/',views.edit_addres,name="edit_addres"),
    path('select_address/<int:id>/',views.select_address,name="select_address"),












]