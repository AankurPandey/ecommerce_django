# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    gender = models.CharField(max_length=1, default='M', null=False)
    email_id = models.CharField(max_length=50, blank=False, null=False)
    cart_id = models.PositiveSmallIntegerField(default=0, null=False)