from django.contrib import admin
from .models import Product, CustomerPurchase

admin.site.register(Product)
admin.site.register(CustomerPurchase)