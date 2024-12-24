from django.contrib import admin
from .models import Categories, Products, Commande, Order, Cart

# Register your models here.
class AdminCategories(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    
class AdminProducts(admin.ModelAdmin):
    list_display = ('title','price','date_added','categories')
class AdminCommande(admin.ModelAdmin):
    list_display = ('items','nom','email','address', 'ville', 'pays','total', 'date_commande', )


admin.site.register(Products, AdminProducts)
admin.site.register(Categories , AdminCategories)
admin.site.register(Commande, AdminCommande) 
admin.site.register(Order)
admin.site.register(Cart)