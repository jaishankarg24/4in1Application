from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

# Create your views here.
from myfood.models import *
from myfood.filters import CityFilter


import json
import datetime


@login_required
def food(request):
    context={}

    filter_restaurant_by_city = CityFilter(request.GET, queryset=Restaurants.objects.all())
    context['filter_restaurant_by_city'] = filter_restaurant_by_city
    return render(request=request, template_name='myfood/basefood.html', context=context)

def login_view(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if request.method=="POST":
    	name=request.POST['username']
    	request.session[name]=name

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('food'))
    else:
    	dict={'message':'Login fail'}
    	return render(request=request, template_name='myfood/login.html', context=dict)


def logout_view(request):

	dict={'message':'Logged out'}
	logout(request)
	return render(request=request, template_name='myfood/login.html', context=dict)


def register_view(request):
 
    if request.method == 'GET':
        return render(request, 'myfood/register.html', {'message': None})
    else:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        request.session[username]=username

        if user is None:
            new_user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('food')) 
        else:
            return render(request, 'myfood/register.html', {'message': 'User already exists.'})

def restaurantDetailView(request, pk):
    #rests = Restaurants.objects.all()
    #restId = request.GET.get('pk')
    menu = MenuItem.objects.filter(restaurant_id=pk)

    my_dict = {'menu': menu}
    return render(request=request, template_name='myfood/menuitem_detail.html', context=my_dict)



