# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-22 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201022_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
