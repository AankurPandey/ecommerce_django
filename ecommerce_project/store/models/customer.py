from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    @classmethod
    def get_customer_by_email(cls, email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    @classmethod
    def get_customer_by_id(cls, id):
        try:
            return Customer.objects.get(pk=id)
        except:
            return False
        


    @classmethod
    def get_customer_id(cls, email):
        try:
            user = Customer.objects.get(email=email)
            return user.id
        except:
            return False

    @classmethod
    def add_customer(cls, obj):
        obj.save()

    @classmethod
    def add_product_to_cart(cls, req):
        item_id = req.POST.get('itemId')

        if req.session.get('cart'):
            cart = req.session['cart']
            if cart.get(item_id):
                cart[item_id] += 1
            else:
                cart[item_id] = 1
        else:
            cart = {item_id: 1}
        
        return cart

    @classmethod
    def remove_product_from_cart(cls, req):
        item_id = req.POST.get('itemId')
        cart = req.session.get('cart')
        cart[item_id] -= 1

        return cart