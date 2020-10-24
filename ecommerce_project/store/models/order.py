from django.db import models
from .product import Product
from .customer import Customer
from datetime import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.today)


    @classmethod
    def place_order(cls, obj):
        obj.save()


    @classmethod
    def get_order_by_customer(cls, user_id):
        return Order.objects.filter(customer=user_id).order_by('-date')
        
