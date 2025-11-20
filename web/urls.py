
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
    path('address/',views.address ,name="address"),
    path('add_address/',views.add_address ,name="add_address"),






    path('add_cart/<int:id>/',views.add_cart,name="add_cart"),
    path('cart_plus/<int:id>/',views.cart_plus,name="cart_plus"),
    path('cart_minies/<int:id>/',views.cart_minies,name="cart_minies"),
    path('cart_incriment/<int:id>/',views.cart_incriment,name="cart_incriment"),
    path('cart_mcart_decrimentinies/<int:id>/',views.cart_decriment,name="cart_decriment"),








]