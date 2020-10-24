from django import template

register = template.Library()


@register.filter(name="in_cart")
def check_item_in_cart(product_id, cart):
    return bool(int(cart.get(str(product_id), '0')))


@register.filter(name="quantity_in_cart")
def get_item_quantity(product_id, cart):
    return cart[str(product_id)]


@register.filter(name="price_total")
def get_total_price(product, cart):
    return cart[str(product.id)]*product.price


@register.filter(name="total_cart_amount")
def get_cart_total(product_list, cart):
    amount = 0

    for product in product_list:
        if str(product.id) in cart:
            amount += product.price * cart[str(product.id)]

    return amount