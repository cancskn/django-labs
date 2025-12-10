"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from restaurants.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_restaurant, name="add_restaurant"),
    path('list/', list_restaurants, name="list_restaurants"),
    path('delete/', delete_page, name="delete_page"),
    path('delete-selected/', delete_selected, name="delete_selected"),
    path('edit/', edit_page, name="edit_restaurants"),
    path('search/', search_restaurant, name="search_restaurant"),

]
