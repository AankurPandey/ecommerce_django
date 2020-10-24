# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'description']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']


class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'product', 'customer', 'quantity', 'price', 'date']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)