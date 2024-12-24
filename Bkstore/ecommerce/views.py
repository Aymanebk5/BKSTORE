from audioop import reverse
from .models import Cart, Order, Products, Categories
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import JsonResponse
from .models import Products
from .models import Contact as ContactModel
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
import logging
    
    
    
def index(request):
    products_objects = Products.objects.all()
    return render(request, 'ecommerce/index.html', {'products_object': products_objects})

def products_view(request):
    products_objects = Products.objects.all()
    return render(request, 'ecommerce/products.html', {'products_object': products_objects})

def products(request, Products_id):
    
    products = Products.objects.get(id=Products_id)
    context = {
        'products': Products,
        'products_id': Products_id
    }
    return render(request, 'products.html', context)

def about(request):
    return render(request, 'ecommerce/ABOUT.html')

def account(request):
    return render(request, 'ecommerce/Account.html')

def Commande(request):
    return render(request, 'ecommerce/Commande.html')

def contact(request):
    return render(request, 'ecommerce/Contact.html')

def confirmation(request):
    return render(request, 'ecommerce/confirmation.html')



def css_view(request):
    css_file = open('path/to/your/css/file.css', 'r')
    return HttpResponse(css_file.read(), content_type='text/css')


def Productdetails(request): 
    return render(request, 'ecommerce/Product-details.html') 

def Productdetails2(request):  
    return render(request, 'ecommerce/Product-details2.html')

def Productdetails3(request): 
    return render(request, 'ecommerce/Product-details3.html')

def ProductdetailsX(request): 
    return render(request, 'ecommerce/Product-detailsX.html')


def products3(request):
    return render(request, 'ecommerce/Products3.html')

def products2(request):
    return render(request, 'ecommerce/Products2.html')

def add_products(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        products = Products(title=title, description=description, price=price)
        products.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'add_products.html')




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = get_user_model()
        user = User.objects.create_user(username, password)
        user.save()
        return redirect('Products.html')
    return render(request,'register.html')


def Account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.error(request, "Incorrect Username or Password. ")
            return redirect('Account')
    return render(request, 'Account.html')


def Contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = ContactModel.objects.create(name=name, email=email, subject=subject, message=message)
        contact.save()
        return render(request, 'confirmation.html')
    else:
        return render(request, 'Contact.html')
    
    


def add_to_cart(request, product_id):
    logging.info('Hello')
    product = Products.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = cartitem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart.html', context={"orders": cart.orders.all()})

def product_list(request):
    sort = request.GET.get('sort', '')
    products = Products.objects.all()
    if sort == 'price':
        products = products.order_by('price')
    elif sort == 'popularity':
        products = products.order_by('-popularity')
    elif sort == 'sale':
        products = products.filter(sale=True)
    elif sort == 'rating':
        products = products.order_by('-rating')
    return render(request, 'product_list.html', {'products': products})
