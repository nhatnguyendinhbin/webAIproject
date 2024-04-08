"""
URL configuration for thuongmaidientu_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include để thêm đường dẫn của các app

urlpatterns = [
    path('admin/', admin.site.urls),
    # thêm đường dẫn cho các app 
    path('', include('Guest_app.urls')),  # Đường dẫn cho ứng dụng "guests"
    # path('Customer/', include('Customer.urls')),  # Đường dẫn cho ứng dụng "customer"
    # path('System/', include('System.urls')),  # Đường dẫn cho ứng dụng "system"
    # path('Seller/', include('Seller.urls')),  # Đường dẫn cho ứng dụng "seller"
]
