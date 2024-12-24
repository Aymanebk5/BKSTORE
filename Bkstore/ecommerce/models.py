import genericpath
from typing import Generic
from webbrowser import GenericBrowser
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.conf import settings 




# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['-date_added']
    
def __str__(self):
    return self.name



class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    categories = models.ForeignKey(Categories, verbose_name=("Categories"), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank = True)
    date_added = models.DateTimeField(auto_now=True)
    
class Meta:
    ordering = ['-date_added']
    
def __str__(self):
    return self.title 



class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom   




class Contact(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    subject = models.CharField(max_length=128, blank=False)
    message = models.TextField(blank=False)
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.name
    


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.products.title} ({self.quantity})"
    
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
 






