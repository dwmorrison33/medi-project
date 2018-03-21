from django.conf.urls import url, include
from medi_project_app import views

urlpatterns = [
    url(r'^products/(?P<id>[0-9]+)/$', views.product_detail, name='product-detail'),
    url(r'^products', views.products, name='list-of-products'),
    url(r'^purchase/(?P<id>[0-9]+)', views.create_purchase, name='create-purchase'),
    url(r'^purchase-complete', views.purchase_complete, name='purchase-complete'),
    url(r'^search/$', views.search, name='search'),
]