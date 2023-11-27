from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    return render(request,"indexEn.html",{})

def gallery(request):
    return render(request,"gallery.html",{})

def img_detail(request):
    return render(request,"photo-detail.html",{})

def products(request):
    theproducts=Product.objects.filter(name="sagi")
    
    return render(request,"product.html",{
        "htmlproducts":theproducts,
    })
