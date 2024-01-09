"""
URL configuration for weather_Max project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from weather_. import views
from django.contrib import admin
import importlib

# Dynamically import the views module from the app

views = importlib.import_module('.views', package='weather_')
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('get_weather/', views.get_weather, name='get_weather'),
]
"""
from .weather_ import views

from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),  # Maps to the "index" view
    path('get_weather/', views.get_weather, name='get_weather'),  # Maps to the "get_weather" view
    # Add more URL patterns as needed
]
"""