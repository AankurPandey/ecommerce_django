from django.conf.urls import url
from .views import index, signup, \
    check_password, login


urlpatterns = [
    url('home/', index),
    url('signup/', signup),
    url('password/', check_password),
    url('login/', login)
]