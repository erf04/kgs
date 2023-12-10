from django.shortcuts import render
from .models import Product

def home(request):
    products=Product.objects.all()[:9]
    return render(request,"home.html",{
        "products":products
    })

def gallery(request):
    return render(request,"gallery.html",{})

def pro_detail(request):
    return render(request,"productDetail.html",{})

def AboutUs(request):
    return render(request,"AboutUs.html",{})

def Contact(request):
    return render(request,"Contact.html",{})\

def products(request):
    theproducts=Product.objects.filter(name="sagi")
    
    return render(request,"product.html",{
        "htmlproducts":theproducts,
    })

def seeproduct(request,id):
    product=Product.objects.get(pk=id)
    return render(request,"productDetail.html",{
        "product":product
    })