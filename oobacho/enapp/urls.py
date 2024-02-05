
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="enhome"),
    path('gallery/',views.gallery,name="gallery"),
    path('productDetail/',views.pro_detail,name="productDetail"),
    path('products/',views.products,name="products"),
    path('AboutUs/',views.AboutUs,name="AboutUs"),
    path('Contact/',views.Contact,name="Contact"),
    path('seeproduct/<int:id>/',views.seeproduct,name="seeproduct"),
    path('resultSearch/',views.result,name="result"),
    path('Events_News/',views.Event_News,name="E_N"),
    path('seeEventsNews/',views.seeEventNews,name="seeEventNews"),
    path('FAQs/',views.FAQs,name="FAQs"),
]