from django.urls import path,re_path

from myshop import views

urlpatterns=[
	path('',views.home, name="home"),
	path('shopping/', views.shopping, name="shop"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('logout/',views.logout_page),  
    path('signup/', views.signup_page),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]