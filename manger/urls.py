
from django.urls import path
from manger import views

app_name ="manger"

urlpatterns = [
    path('',views.index ,name="index"),
    path('manager_header/',views.manager_header ,name="manager_header"),

    


]