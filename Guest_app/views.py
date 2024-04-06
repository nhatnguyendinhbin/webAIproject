from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return render(request, 'Guest_app/home.html')

# add product bằng admin của Django

# list phone:
def list_iphone(request):
    iphone = Product.objects.all()
    context = {'iphone':iphone}
    return render(request , 'Guest_app/dien_thoai/iphone/iphone.html',context)

def list_samsung(request):
    samsung = Product.objects.all()
    context = {'samsung':samsung}
    return render(request , 'Guest_app/dien_thoai/samsung/samsung.html',context)

def list_xiaomi(request):
    xiaomi = Product.objects.all()
    context = {'xiaomi':xiaomi}
    return render(request , 'Guest_app/dien_thoai/xiaomi/xiaomi.html',context)

def details(request):
    return render(request, 'Guest_app/details.html')