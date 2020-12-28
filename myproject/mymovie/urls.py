from django.urls import path

from mymovie import views

urlpatterns =[
	path('movie/', views.movie, name='movie'),
	path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),

    path('theatre/<int:pk>/', views.theatreDetailView, name='theatre_detail'),
]