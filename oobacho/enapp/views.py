from django.shortcuts import render,redirect
from .models import Product, Certification
from django.http import HttpRequest
from django.contrib import messages
from .forms import ProductForm

def home(request):
    products=Product.objects.all()[:3]
    products2=Product.objects.all()[:9]
    cer=Certification.objects.all()[:9]
    myrange=range(1,4)
    final=zip(products,myrange)
    return render(request,"home.html",{
        "products":final,
        "products2":products2,
        "certifications":cer,
    })

def gallery(request):
    return render(request,"gallery.html",{})

def pro_detail(request):
    return render(request,"productDetail.html",{})

def AboutUs(request):
    return render(request,"AboutUs.html",{})

def Contact(request):
    return render(request,"Contact.html",{})

def Event_News(request):
    return render(request,"Event_News.html",{})

def seeEventNews(request):
    return render(request,"seeEventNews.html",{})

def products(request):
    theproducts=Product.objects.filter(name="sagi")
    
    return render(request,"product.html",{
        "htmlproducts":theproducts,
    })

def seeproduct(request:HttpRequest,id):
    product=Product.objects.get(pk=id)
    return render(request,"productDetail.html",{
        "product":product
    })

def FAQs(request):
    return render(request,"FAQs.html",{})

def result(request:HttpRequest):
    searchresult=request.POST.get("searchvalue")
    searchedproducts=Product.objects.filter(name__contains=searchresult)
    if (len(searchresult)) == 0:
        return render(request, "resultSearch.html")
    if len(searchedproducts)==0:
        messages.success(request, "No product found for search \"" + searchresult + "\"")
    else:    
        messages.success(request, "Result for search \"" + searchresult + "\":")
    return render(request,"resultSearch.html",{
        "products":searchedproducts 
    })


def update_product(request:HttpRequest,id):
    product=Product.objects.get(pk=id)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,"your product updated successfully")
            return redirect("enhome")
        else:
            print(form.errors)
        
    form=ProductForm(instance=product) 
    return render(request,"update-product.html",{"form":form,"product":product})


