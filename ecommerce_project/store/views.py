# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.hashers import \
    make_password, check_password
from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order

# Create your views here.
def index(request):
    if request.method == "GET":
        product_list = Product.get_all_products() if not request.GET.get('category') \
            else Product.get_all_products_by_category(request.GET.get('category'))
        content = {
            'productList': product_list,
            'categories': Category.get_all_categories(),
        }
        return render(request, 'orders/index.html', content)
    
    remove = request.POST.get('remove', 0) 
    cart = Customer.remove_product_from_cart(request) if remove else Customer.add_product_to_cart(request)
    
    request.session['cart'] = cart
    return redirect(index)


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
    Customer.add_customer(user)

    user_id = Customer.get_customer_id(email)

    request.session['customerId'] = user_id
    request.session['cart'] = {'1': 0}
    return render(request, 'orders/index.html')


def login(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        return render(request, 'orders/login.html', {'email': email})
    email = request.POST.get('email')
    
    if Customer.get_customer_by_email(email):
        return render(request, 'orders/password.html', {'email': email})

    return render(request, 'orders/signup.html', {'email': email})


def password(request):
    if request.method == "GET":
        email = request.GET.get('email')
        return render(request, 'orders/password.html', {'email': email})

    email = request.POST.get('email')
    password = request.POST.get('password')
    user = Customer.get_customer_by_email(email)

    if check_password(password, user.password):
        request.session['customerId'] = user.id
        request.session['cart'] = {'1': 0}
        return redirect(index)

    error_msg = "Enter the correct Password"
    return render(request, 'orders/password.html', {'error': error_msg, 'email': email})


def do_logout(request):
    request.session.clear()
    return redirect(index)


def get_selected_products(cart):
    pid_list = [i for i in cart.keys() if cart[i]!=0]
    product_list = Product.get_products_by_id(pid_list)
    return product_list 


def cart(request):
    cart = request.session.get('cart')
    product_list = get_selected_products(cart)
    return render(request, 'orders/cart.html', {'productList': product_list})

    
def order(request):
    customer_id =  request.session.get('customerId')
    cart = request.session.get('cart')
    product_list = get_selected_products(cart)

    for product in product_list:
        order = Order(
                product = product,
                customer = Customer.get_customer_by_id(customer_id),
                quantity = cart[str(product.id)],
                price = product.price,
            )
        Order.place_order(order)
    else:
        request.session['cart'] = {'1': 0}
    return redirect(order_view)


def order_view(request):
    customer_id = request.session.get('customerId')
    order_list = Order.get_order_by_customer(customer_id)
    return render(request, 'orders/order.html', {'orderList': order_list})
