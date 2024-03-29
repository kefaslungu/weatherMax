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
import importlib
from django.contrib import admin
from django.urls import path

# Dynamically import the views module from the app
views = importlib.import_module('.views', package='weather_')
view = importlib.import_module('.views', package='weatherforecast')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('weatherforecast/', view.get_weatherforecast, name='forecast'),
]
