from django.shortcuts import render,redirect
from .models import Product, Certification,Event,Category,Type
from django.http import HttpRequest
from django.contrib import messages
from .forms import ProductForm,EventForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
    events=Event.objects.all()

    return render(request,"Event_News.html",{
        "events":events
    })

def seeEventNews(request,id):
    event = Event.objects.get(pk=id)
    return render(request,"seeEventNews.html",{
        "event":event
    })

def getZip():
    categories=Category.objects.all()
    types=[]
    temp=[]
    for cat in categories:
        pros=Product.objects.filter(category=cat)
        for pro in pros:
            if pro.type not in temp:
                temp.append(pro.type)
        types.append(temp)

    filter_result=zip(categories,types)
    return filter_result

def products(request:HttpRequest):
    
    filter_result=getZip()

    products=Product.objects.all()  
    return render(request,"product.html",{
        "products":products,
        "result":filter_result
    })

    # else:
    #     category_id=request.POST["category_id"]
    #     type_id=request.POST["type_id"]
    #     products=Product.objects.filter(category__id=category_id).filter(type__id=type_id)
    #     return render(request,"filtered-products.html",{
    #         "result":filter_result,
    #         "products":products,
    #     })



    


def filter_product(request:HttpRequest,cat_id,type_id):
    filter_result=getZip()
    products=Product.objects.filter(category__id=cat_id).filter(type__id=type_id)
    return render(request,"product.html",{
        "products":products,
        "result":filter_result
    })

def seeproduct(request:HttpRequest,id):
    product=Product.objects.get(pk=id)
    relatedProducts = Product.objects.filter(type=product.type).exclude(pk=id)[:8] 
    return render(request,"productDetail.html",{
        "product":product,
        "related":relatedProducts,
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


@login_required(login_url='/accounts/login')
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


def delete_product(request:HttpRequest,id):
    product=Product.objects.get(pk=id)
    product.delete()
    messages.error(request,"Your Product has been deleted Successfully!")
    return redirect("enhome")


def create_product(request:HttpRequest):
    
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"your product created successfully")
            return redirect("enhome")
        else:
            messages.error(request,"something wrong")
            print(form.errors)    

    form=ProductForm
    return render(request,"create-product.html",{
        "form":form
    })


def create_event(request:HttpRequest,*args,**kwargs):
    if request.method=="POST":
        form=EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"your event created successfully")
            return redirect("enhome")
        else:
            messages.error(request,"something wrong")
            print(form.errors) 

    else:
        form=EventForm
    return  render(request,'eventForm.html',{'form':form},*args,**kwargs)


def delete_event(request:HttpRequest,id):
    instance=Event.objects.get(pk=id)
    instance.delete()
    messages.success(request,"Your Event has been deleted Successfully!")
    return redirect("enhome")


def update_event(request:HttpRequest,id):
    event=Event.objects.get(pk=id)
    if request.method=="POST":
        form=EventForm(request.POST,request.FILES,instance=event)
        if form.is_valid():
            form.save()
            messages.success(request,"your event updated successfully")
            return redirect("enhome")
        else:
            print(form.errors)
        
    form=EventForm(instance=event) 
    print(event.date)
    # print(form.date)
    return render(request,"update_event.html",{"form":form,"event":event})
