from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"indexEn.html",{})

def gallery(request):
    return render(request,"gallery.html",{})

def img_detail(request):
    return render(request,"photo-detail.html",{})
