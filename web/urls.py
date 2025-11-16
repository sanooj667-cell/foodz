
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
    path('add_cart/<int:id>/',views.add_cart,name="add_cart"),
    path('cart_plus/<int:id>/',views.cart_plus,name="cart_plus"),







]