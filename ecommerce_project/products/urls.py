from django.conf.urls import url
from . import views


urlpatterns = [
    url('list/', views.product_list, name='product_list'),
    url('add/', views.product_add, name='product_add'),
    url('<int:id>/update', views.update_product, name='product_update')
]