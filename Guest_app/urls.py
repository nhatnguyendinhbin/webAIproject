# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # list phone
    path('list_iphone/', views.list_iphone , name= 'list_iphone'),
    path('list_samsung/', views.list_samsung , name= 'list_samsung'),
    path('list_xiaomi/', views.list_xiaomi , name= 'list_xiaomi'),

    # chi tiết sản phẩm
    path('detail_product/<int:id>/', views.detail_product, name='detail_product'),
    # giỏ hàng
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    # thanh toán
    path('check_out/', views.check_out, name='check_out'),
    # xóa khỏi giỏ hàng
    path('remove_product/<int:id>/', views.remove_product, name='remove_product'),
    
]