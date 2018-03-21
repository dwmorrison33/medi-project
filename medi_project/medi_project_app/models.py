from django.db import models

import uuid

class Product(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=254)
    product_type = models.CharField(max_length=254)
    cost = models.IntegerField()
    description = models.CharField(max_length=254)
    pushed_product = models.BooleanField(default=False)
    callback = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    inventory_on_hand = models.IntegerField(default=1)
    photo = models.FileField(upload_to='products')

    def __str__(self):
        return self.name


class CustomerPurchase(models.Model):
    product_name = models.CharField(max_length=254)
    product_price = models.IntegerField()
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)
    email = models.EmailField()
    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name