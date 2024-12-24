from django.urls import path
from django.contrib import admin
from ecommerce.views import index,add_to_cart, products, cart
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index, name='index'),
    path('admin/', admin.site.urls),
    path('index.html',views.index, name='index'),
    path('add-to-cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('cart.html', views.cart, name='cart'),
    path('Products.html',views.products_view, name='products'),
    path('ABOUT.html',views.about, name='about'),
    path('Contact.html', views.Contact, name='Contact'),
    path('Commande.html',views.Commande, name='commande'),
    path('confirmation.html',views.confirmation, name='confirmation'),
    path('Products2.html',views.products2, name='products2'),
    path('Products3.html',views.products3, name='products3'),
    path('css/', views.css_view, name='css_view'),
    path('Product-details.html',views.Productdetails, name='Product-details'), 
    path('Product-details2.html',views.Productdetails2, name='Product-details2'), 
    path('Product-details3.html',views.Productdetails3, name='Product-details3'), 
    path('Product-detailsX.html',views.ProductdetailsX, name='Product-detailsX'), 
    path('register.html', views.register, name='register'),
    path('Account.html', views.Account, name='Account'),
    path('confirmation/', views.confirmation, name='confirmation'),
 

    
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
