# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SellerModel(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    gender = models.CharField(max_length=1, default='M', null=False)
    office_address = models.CharField(max_length=120, blank=True, null=True)