from django.conf.urls import url
from .views import index, signup, cart, \
    password, login, do_logout


urlpatterns = [
    url('home/', index),
    url('signup/', signup),
    url('password/', password),
    url('login/', login),
    url('logout/', do_logout),
    url('cart/', cart)
]