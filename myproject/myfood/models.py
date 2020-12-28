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

class Restaurants(models.Model):
	restaurant_name = models.CharField(max_length=50) 
	area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE, related_name="area")
	city = models.ForeignKey(City, null=True, on_delete=models.CASCADE, related_name="city")
	restaurant_img = models.ImageField(null=True, blank=True)
	
class MenuItem(models.Model):
	food_name = models.CharField(max_length=50) 
	restaurant = models.ForeignKey(Restaurants, null=True, on_delete=models.CASCADE, related_name="restaurant")
	image = models.ImageField(null=True, blank=True)
	price = models.DecimalField( max_digits=5, decimal_places=2, default=0)

class Order(models.Model):
	customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="orders")
	date = models.DateTimeField(auto_now=True)
	in_cart = models.BooleanField(default=True)
	placed = models.BooleanField(default=False)
	completed = models.BooleanField(default=False)




class OrderItem(models.Model):
	menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True, related_name="menuitems")
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name="orders")
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)


class DeliveryAddress(models.Model):
	customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)
    
class FoodCustomer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name