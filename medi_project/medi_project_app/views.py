from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .models import Product, CustomerPurchase
from .forms import CustomerForm

import random, string

def products(request):
    products = Product.objects.all()
    context = {
    	"products": products
    }
    return render(request, 'products.html', context)

def product_detail(request, id):
	product = Product.objects.get(id=id)
	context = {
		"product": product
	}
	return render(request, 'product_detail.html', context)

def create_purchase(request, id):
	product = Product.objects.get(id=id)
	form = CustomerForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			# random confirmation_code
			confirmation_code = ''.join(
				[random.choice(string.ascii_letters + string.digits)
				for x in range(6)
				]
			)
			purchase_form = form.save(commit=False)
			purchase_form.product_price = product.cost
			purchase_form.product_name = product.name
			purchase_form.confirmation_code = confirmation_code
			purchase_form.save()
			#update the inventory for item purchased
			product.inventory_on_hand = product.inventory_on_hand - 1
			product.save()
			messages.success(request, "You have successfully purchased " + product.name)
			return redirect('purchase-complete')
		else:
			messages.error(
				request,
				"It looks like you didn't fill out the form correctly, Please try again."
			)
			form = CustomerForm()
	context = {
		'form': form,
		'product': product,
	}
	return render(request, 'create_purchase.html', context)

def purchase_complete(request):
	return render(request, 'purchase_complete.html', {})

def search(request):
    products = Product.objects.filter(name__contains=request.GET['name'])
    return render(request, 'products.html', {"products": products})