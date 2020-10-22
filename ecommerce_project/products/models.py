# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    discount = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False)
    quantity = models.PositiveSmallIntegerField(default=0, null=False)
    available = models.BooleanField(default=True, null=False)
    category = models.CharField(max_length=10, blank=False, null=False)
    seller_id = models.PositiveSmallIntegerField(blank=False, null=False)
    # image = models.ImageField()