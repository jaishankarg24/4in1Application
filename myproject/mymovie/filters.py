import django_filters
from mymovie.models import Theatres

class CityFilter(django_filters.FilterSet):
	class Meta:
		model = Theatres
		fields=['city']
	