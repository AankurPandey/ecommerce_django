from django import template

register = template.Library()


@register.filter(name="in_cart")
def check_item_in_cart(product_id, cart):
    return bool(int(cart.get(str(product_id), '0')))


@register.filter(name="quantity_in_cart")
def return_item_quantity(product_id, cart):
    return cart[str(product_id)]