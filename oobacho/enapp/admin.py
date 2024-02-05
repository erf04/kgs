from django.contrib import admin
from .models import Product,Certification,Type,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Certification)
admin.site.register(Category)
admin.site.register(Type)

