from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_datetime),
    path('multiplication/', views.multiplication_table),
    path('day/', views.day_of_programmer),
]