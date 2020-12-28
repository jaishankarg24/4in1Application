from django.contrib import admin

# Register your models here.
from mymovie.models import *

class CityAdmin(admin.ModelAdmin):
	list_display=['city_name']
admin.site.register(City, CityAdmin)

class AreaAdmin(admin.ModelAdmin):
	list_display=['area_name']
admin.site.register(Area, AreaAdmin)


admin.site.register(MovieCustomer)
admin.site.register(Theatres)


admin.site.register(Movies)


admin.site.register(Book)


admin.site.register(BookTicket)


admin.site.register(TicketInfo)