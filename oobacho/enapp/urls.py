
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="enhome"),
    path('gallery/',views.gallery,name="gallery"),
    path('photo-detail/',views.img_detail,name="photo-detail"),
    
]