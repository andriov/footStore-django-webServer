from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list', views.ProductList.as_view(), name='product-list'),
]
