from django.shortcuts import render

# Create your views here.

def index(request):

    return render (request,"admin/index.html")






def manager_header(request):

    return render(request,"admin/manager-header_fooddz.html")
