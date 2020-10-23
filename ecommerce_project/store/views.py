# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.hashers import \
    make_password, check_password
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


# Create your views here.
def index(request):
    product_list = Product.get_all_products() if not request.GET.get('category') \
        else Product.get_all_products_by_category(request.GET.get('category'))
    content = {
        'productList': product_list,
        'categories': Category.get_all_categories(),
    }
    return render(request, 'orders/index.html', content)


def signup(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        return render(request, 'orders/signup.html', {'email': email})

    name = request.POST.get('name')
    email = request.POST.get('email')
    error_msg = None

    if len(request.POST.get('password'))<=5:
        error_msg = "Your password length should be grater than 5 character"
    else:
        password = make_password(request.POST.get('password'))

    if error_msg:
        content = {
        'error': error_msg,
        'name': name,
        'email': email
    }
        return render(request, 'orders/signup.html', content)

    user = Customer(name=name, email=email, password=password)
    user.save()
    
    return render(request, 'orders/index.html')


def login(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        return render(request, 'orders/login.html', {'email': email})
    email = request.POST.get('email')
    
    if Customer.get_customer_by_email(email):
        return render(request, 'orders/password.html', {'email': email})

    return render(request, 'orders/signup.html', {'email': email})


def check_password(request):
    if request.method == "GET":
        email = request.GET.get('email')
        return render(request, 'orders/password.html', {'email': email})

    email = request.POST.get('email')
    password = request.POST.get('password')
    user = Customer.get_customer_by_email(email)

    if check_password(password, user.password):
        request.session['customer_id'] = user.id
        request.session['customer_email'] =user.email
        return render(request, 'orders/index.html')

    error_msg = "Enter the correct Password"
    return render(request, 'orders/password.html', {'error': error_msg, 'email': email})

