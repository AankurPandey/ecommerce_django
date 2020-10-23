# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .form import ProductForm
from .models import ProductModel
import pdb

# Create your views here.
def product_list(request):
    context = {'productList': ProductModel.objects.all()[1:]}
    return render(request, 'products/list.html', context)


def product_add(request):
    if request.method == "GET":
        form = {'form': ProductForm()}
        return render(request, '/products/form.html',form)

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('/products/list')


def update_product(request, my_id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/list.html", context)
