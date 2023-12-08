
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="enhome"),
    path('gallery/',views.gallery,name="gallery"),
    path('productDetail/',views.pro_detail,name="productDetail"),
    path('products/',views.products,name="products"),
    path('AboutUs/',views.AboutUs,name="AboutUs"),
    path('seeproduct/<int:id>/',views.seeproduct,name="seeproduct"),
]