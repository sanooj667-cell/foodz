
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

    



    
    

]