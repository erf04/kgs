
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
    path('seeEventsNews/<int:id>/',views.seeEventNews,name="seeEventNews"),
    path('FAQs/',views.FAQs,name="FAQs"),
    path("update_product/<int:id>/",views.update_product,name="update-product"),
    path("create_product/",views.create_product,name="create-product"),
    path("delete_product/<int:id>/",views.delete_product,name='delete-product'),
    path('create_event/',views.create_event,name="create-event"),
    path('update_event/<int:id>/',views.update_event,name="update-event"),
    path('delete/<int:id>/',views.delete_event,name="delete-event"),
    path('filtered_products/<int:cat_id>/<int:type_id>/',views.filter_product,name="filtered-products"),

]