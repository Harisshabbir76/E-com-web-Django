from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    image1=models.ImageField()
    image2=models.ImageField()
    image3=models.ImageField()
    slug=models.SlugField(default="unknown")

    def __str__(self):
        return self.title
    
    def snippit(self):
        return self.desc[:180]+'...'
    

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"Order for {self.product.title} by {self.name}"



class CartItem(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"