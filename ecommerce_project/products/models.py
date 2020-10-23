# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class ProductModel(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    discount = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False)
    quantity = models.PositiveSmallIntegerField(default=0, null=False)
    available = models.BooleanField(default=True, null=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    # seller_id = models.PositiveSmallIntegerField(blank=False, null=False)
    # image = models.ImageField()

    def get_absolute_url(self):
        return reverse("products:product_update", kwargs={"my_id": self.id})