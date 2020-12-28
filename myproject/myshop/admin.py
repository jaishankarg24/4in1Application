from django.contrib import admin

# Register your models here.

from myshop.models import *

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'information', 'image', 'category']

admin.site.register(Product, ProductAdmin)



class CategoryAdmin(admin.ModelAdmin):
	list_display=['name']

admin.site.register(Category, CategoryAdmin)


class CustomerAdmin(admin.ModelAdmin):
	list_display = ['user','name', 'email']
admin.site.register(Customer, CustomerAdmin)


class OrderAdmin(admin.ModelAdmin):
	list_display = ['customer', 'date_ordered', 'complete', 'transaction_id']
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['product', 'order', 'quantity', 'date_added']
admin.site.register(OrderItem, OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
	list_display = ['customer', 'order', 'address', 'city', 'state', 'pincode', 'date_added']
admin.site.register(ShippingAddress)