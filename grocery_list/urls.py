from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/new', views.users_new), # to create user
    path('stores/new', views.stores_new), # to create a store
    path('products/new', views.products_new) # to create a product
]