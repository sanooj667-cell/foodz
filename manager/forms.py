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