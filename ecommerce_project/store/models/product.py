from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='upload/products_images/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_id(id_list):
        return Product.objects.filter(id__in=id_list)

    @staticmethod
    def get_all_products_by_category(category):
        return Product.objects.filter(category=category)
