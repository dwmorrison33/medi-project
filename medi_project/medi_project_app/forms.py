from django.forms import ModelForm
from .models import Product, CustomerPurchase

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
        	'name', 'code', 'product_type',
        	'cost', 'description', 'pushed_product',
        	'callback', 'category', 'inventory_on_hand', 'photo'
        ]


class CustomerForm(ModelForm):
    class Meta:
        model = CustomerPurchase
        fields = [
        	'name', 'email', 'address', 'phone'
        ]