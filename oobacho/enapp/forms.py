from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-select"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "type":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"})
        }