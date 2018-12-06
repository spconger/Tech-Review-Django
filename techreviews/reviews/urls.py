from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getProducts', views.getProducts, name='products'),
    path('productdetail/<int:id>', views.productdetail, name='productdetail'),


]