# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CartModel(models.Model):
    product_id_list = models.TextField()