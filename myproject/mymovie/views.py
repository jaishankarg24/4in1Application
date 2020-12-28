from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

# Create your views here.
from mymovie.models import *
from mymovie.filters import CityFilter


import json
import datetime

@login_required()
def movie(request):
	context={}
	filter_theatre_by_city = CityFilter(request.GET, queryset=Theatres.objects.all())
	context['filter_theatre_by_city'] = filter_theatre_by_city
	return render(request=request, template_name='mymovie/movie.html', context=context)

def login_view(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if request.method=="POST":
    	name=request.POST['username']
    	request.session[name]=name

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('movie'))
    else:
    	dict={'message':'Login fail'}
    	return render(request=request, template_name='mymovie/login.html', context=dict)


def logout_view(request):

	dict={'message':'Logged out'}
	logout(request)
	return render(request=request, template_name='mymovie/login.html', context=dict)


def register_view(request):
 
    if request.method == 'GET':
        return render(request, 'mymovie/register.html', {'message': None})
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
            return HttpResponseRedirect(reverse('movie')) 
        else:
            return render(request, 'mymovie/register.html', {'message': 'User already exists.'})


def theatreDetailView(request, pk):

    movie = Movies.objects.filter(theatre_id=pk)

    my_dict = {'movie': movie}
    return render(request=request, template_name='mymovie/movie_detail.html', context=my_dict)