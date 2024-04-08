# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # list phone
    path('list_iphone/', views.list_iphone , name= 'list_iphone'),
    path('list_samsung/', views.list_samsung , name= 'list_samsung'),
    path('list_xiaomi/', views.list_xiaomi , name= 'list_xiaomi'),
    # detail cart
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('check_out/', views.check_out, name='check_out'),
    # <int:id>
    
]