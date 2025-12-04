from django import forms
from restaurent.models import *


class StoreCategoryForm(forms.ModelForm):
    class Meta:
        model = Storecategory
        fields = ["name","image"]




        widgets = { 
            "name" : forms.widgets.TextInput(attrs={"class": "form_control", "placehold":"Category name"}),
            "image" : forms.widgets.FileInput(attrs={"class":"form_control"})
        }





class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name","image","catagorey","tagline","rating","time",]




        widgets = { 
            "name" : forms.widgets.TextInput(attrs={"class": "form_control", "placehold":"Category name"}),
            "catagorey" : forms.widgets.Select(attrs={"class": "form_control"}),
            "tagline" : forms.widgets.TextInput(attrs={"class": "form_control", "placehold":"Tag line"}),
            "rating" : forms.widgets.TextInput(attrs={"class": "form_control", "placehold":"Rating"}),
            "time" : forms.widgets.TextInput(attrs={"class": "form_control", "placehold":"Time"}),
            "image" : forms.widgets.FileInput(attrs={"class":"form_control"})
        }




class FoodCtegoryForm(forms.ModelForm):
    class Meta:
        model = FoodCatagory
        fields = ["name","store"]


        widgets = {
            "name" :forms.widgets.TextInput(attrs={"class":"form_control", "placehold":"Category name"}),
            "store" :forms.widgets.Select(attrs={"class":"form_control"})

        }



class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItems
        fields = ["name","image","price","category","store","is_veg",]

        widgets = {
            "name" : forms.widgets.TextInput(attrs={"class":"form_control", "placehold":"Item name"}),
            "image" : forms.widgets.FileInput(attrs={"class":"form_control"}),
            "price" : forms.widgets.TextInput(attrs={"class":"form_control", "placehold":"Item price"}),
            "category" : forms.widgets.Select(attrs={"class":"form_control"}),
            "store" : forms.widgets.Select(attrs={"class":"form_control"}),
            "is_veg": forms.widgets.CheckboxInput(attrs={"class":"form_control"})
        }


     