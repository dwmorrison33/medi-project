from django.core.urlresolvers import resolve
from django.test import TestCase, RequestFactory
from django.http import HttpRequest

from medi_project_app.views import (
	products, product_detail, create_purchase, purchase_complete
)
from medi_project_app.models import Product, CustomerPurchase

#test responses
class ProductListTest(TestCase):
    def test_products(self):
        resp = self.client.get('/products')
        self.assertEqual(resp.status_code, 200)

class ProductDetailTest(TestCase):
	def test_product_detail(self):
		resp1 = self.client.get('/products/2')
		self.assertEqual(resp1.status_code, 200)

class PurchasePageCompleteTest(TestCase):
	def test_purchase_complete(self):
		resp = self.client.get('/purchase-complete')
		self.assertEqual(resp.status_code, 200)