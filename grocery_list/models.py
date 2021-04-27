from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    # stores - tracks what stores this user created
    # products - tracks what products this user created
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    creator = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    # stores - this is a list of stores that this product is stocked at.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Store(models.Model):
    name = models.CharField(max_length=45)
    creator = models.ForeignKey(User, related_name='stores', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='stores')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)