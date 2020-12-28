from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.conf import settings

class City(models.Model):
	city_name = models.CharField( max_length=50)

	def __str__(self):
		return self.city_name

class Area(models.Model):
	area_name = models.CharField(max_length=50)

	def __str__(self):
		return self.area_name

class MovieCustomer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Theatres(models.Model):
	theatre_name = models.CharField(max_length=50) 
	area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE, related_name="area")
	city = models.ForeignKey(City, null=True, on_delete=models.CASCADE, related_name="city")
	theatre_img = models.ImageField(null=True, blank=True)
	
class Movies(models.Model):
	movie_name = models.CharField(max_length=50) 
	theatre = models.ForeignKey(Theatres, null=True, on_delete=models.CASCADE, related_name="theatre")
	image = models.ImageField(null=True, blank=True)
	language = models.CharField(max_length=50,null=True, blank=True) 
	show_time = models.CharField(max_length=50,null=True, blank=True)
	price = models.DecimalField( max_digits=5, decimal_places=2, default=0)

class Book(models.Model):
	movie_customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="movie_customer")
	date = models.DateTimeField(auto_now=True)
	booked = models.BooleanField(default=False)

class BookTicket(models.Model):
	movie = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True, related_name="movie")
	book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name="book")
	seats = models.IntegerField(default=1, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)


class TicketInfo(models.Model):
	movie_customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	book_ticket = models.ForeignKey(BookTicket, on_delete=models.SET_NULL, null=True, related_name="book_ticket")
	date_added = models.DateTimeField(auto_now_add=True)
    
