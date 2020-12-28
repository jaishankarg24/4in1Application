import django_filters
from myfood.models import Restaurants

class CityFilter(django_filters.FilterSet):
	class Meta:
		model = Restaurants
		fields=['city']
	