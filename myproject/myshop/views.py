from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from myshop.models import *


from django.contrib.auth.decorators import login_required
from myshop.forms import SignupForm
from django.http import HttpResponseRedirect

import json
import datetime

def home(request):
	return render(request=request, template_name='myshop/home.html')

@login_required
def shopping(request):

	if request.user.is_authenticated:
		customer= request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items=order.orderitem_set.all()
		cartItem = order.get_cart_items

	products = Product.objects.all()
	categories = Category.objects.all() 
	my_dict={'products': products, 'categories': categories, 'cartItem':cartItem}
	return render(request=request, template_name='myshop/shopping.html', context=my_dict)



def cart(request):
	if request.user.is_authenticated:
		customer= request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items=order.orderitem_set.all()				
		cartItem = order.get_cart_items

	my_dict = {'items': items, 'order': order, 'cartItem':cartItem}
	return render(request=request, template_name='myshop/cart.html', context=my_dict)

def checkout(request):
	if request.user.is_authenticated:
		customer= request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items=order.orderitem_set.all()
		cartItem = order.get_cart_items
			
	my_dict = {'items': items, 'order': order, 'cartItem':cartItem}
	return render(request=request, template_name='myshop/checkout.html', context=my_dict)



def logout_page(request):
	request.session.clear()
	return render(request=request, template_name='myshop/logout.html')


def signup_page(request):
	form=SignupForm()
	my_dict={'form':form}

	if request.method=="POST":

		name=request.POST['username']
		request.session[name]=name
		

		form=SignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
		return HttpResponseRedirect('/accounts/login/')

	return render(request=request, template_name='myshop/signup.html',context=my_dict)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		pincode=data['shipping']['pincode'],
		)

	return JsonResponse('Payment submitted..', safe=False)