# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'description']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)