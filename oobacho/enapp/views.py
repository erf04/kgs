from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    products=Product.objects.all()[:9]
    return render(request,"indexEn.html",{
        "products":products
    })

def gallery(request):
    return render(request,"gallery.html",{})

def img_detail(request):
    return render(request,"photo-detail.html",{})

def AboutUs(request):
    return render(request,"AboutUs.html",{})

def products(request):
    theproducts=Product.objects.filter(name="sagi")
    
    return render(request,"product.html",{
        "htmlproducts":theproducts,
    })

def seeproduct(request,id):
    product=Product.objects.get(pk=id)
    return render(request,"photo-detail.html",{
        "product":product
    })