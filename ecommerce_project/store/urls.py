from django.conf.urls import url
from .views import index, signup, cart, order, \
    password, login, do_logout, order_view
from .middlewares.auth import auth_middleware


urlpatterns = [
    url('home/', index),
    url('signup/', signup),
    url('password/', password),
    url('login/', login),
    url('logout/', do_logout),
    url('cart/', cart),
    url('create_orders/', auth_middleware(order)),
    url('orders/', auth_middleware(order_view))
]