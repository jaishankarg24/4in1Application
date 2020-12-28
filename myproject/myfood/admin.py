from django.contrib import admin

# Register your models here.
from myfood.models import *

class CityAdmin(admin.ModelAdmin):
	list_display=['city_name']
admin.site.register(City, CityAdmin)

class AreaAdmin(admin.ModelAdmin):
	list_display=['area_name']
admin.site.register(Area, AreaAdmin)

admin.site.register(FoodCustomer)


admin.site.register(Restaurants)

admin.site.register(MenuItem)

admin.site.register(Order)


admin.site.register(OrderItem)

admin.site.register(DeliveryAddress)

