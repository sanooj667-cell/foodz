
from django.urls import path
from manager import views

app_name ="manager"

urlpatterns = [
    path('',views.index ,name="index"),
    path('store_category/',views.store_category ,name="store_category"),
    path('slider/',views.slider ,name="slider"),

    path('store/',views.store ,name="store"),
    path('store_category_creat/',views.store_category_creat ,name="store_category_creat"),
    path('store_category_delete/<int:id>/',views.store_category_delete ,name="store_category_delete"),



    
    

]