from django.db import models

# Create your models here.

class Category(models.Model):
    title =models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.title
    

class Type(models.Model):
    title=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
    

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to="mediafiles/product/")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    type=models.ForeignKey(Type,on_delete=models.CASCADE,related_name="products")
    price=models.DecimalField(max_digits=8,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.name} : {self.type.title}"
    

class Certification(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="mediafiles/certification/")

    def __str__(self) -> str:
        return self.title   


    