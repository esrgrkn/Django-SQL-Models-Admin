
from django.db import models





# Create your models here.

class ProductType(models.Model):
     product_name=models.CharField(max_length=100)
     description=models.CharField(max_length=200)
     def __str__(self):
        return self.product_name

class Supplier(models.Model):
     supplier_name=models.CharField(max_length=100)
     supplierCompany=models.CharField(max_length=100)
     supplierAdress=models.CharField(max_length=100)
     def __str__(self):
        return f"{self.supplier_name} {self.supplierCompany}"

class Product(models.Model):
     product_name=models.CharField(max_length=100)
     product_type=models.CharField(max_length=100)
     description=models.CharField(max_length=200)
     price=models.DecimalField(max_digits=8, decimal_places=2)
     stockStatus = models.BooleanField(default=False)
     slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
     photoLoad=models.ImageField(blank=True)
     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,null=True)
     fruitType=models.ManyToManyField(ProductType)
     interestedFruit=models.BooleanField(default=False)

     def __str__(self):
        return f"{self.product_name} {self.price} {self.slug}"

class ContactForm(models.Model):
   name=models.CharField(max_length=100)
   telephone=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   mesagges=models.CharField(max_length=100)

   def __str__(self):
         return f"{self.name}"
        

