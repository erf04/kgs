from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to="mediafiles/product/")

    def __str__(self) -> str:
        return self.name
    

class Certification(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="mediafiles/certification/")

    def __str__(self) -> str:
        return self.title   


    