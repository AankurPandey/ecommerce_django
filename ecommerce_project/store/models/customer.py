from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    @classmethod
    def get_customer_by_email(cls, email):
        try:
            user = Customer.objects.get(email=email)
            return user
        except:
            return False

