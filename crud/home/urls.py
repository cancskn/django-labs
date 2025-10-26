from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data, name='datapage'),
    path('add-data', views.index, name='homepage'),
    path('delete/<int:person_id>/', views.delete_data, name='delete_data'),
    path('update/<int:person_id>/', views.update_data, name='update_data'),
]
