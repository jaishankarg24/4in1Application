from django.urls import path

from myfood import views

#from myfood.views import RestaurantDetailView

urlpatterns=[

	path('food/', views.food, name='food'),

	path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),

	path('restaurant/<int:pk>/', views.restaurantDetailView, name='restaurant_detail'),
	
	
]