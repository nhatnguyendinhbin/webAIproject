# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_iphone', views.list_iphone , name= 'list_iphone'),
    path('list_samsung', views.list_samsung , name= 'list_samsung'),
    path('list_xiaomi', views.list_xiaomi , name= 'list_xiaomi'),
    path('details', views.details, name='details'),
]