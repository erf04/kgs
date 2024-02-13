from django import forms
from django.forms import ModelForm
from .models import Product,Event


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "type":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"})
        }


class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            #'date': forms.DateField(required=False,format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            "voice":forms.FileInput(attrs={"class":"form-control"}),
            "attachment":forms.FileInput(attrs={"class":"form-control"})
        }
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'})
    )

