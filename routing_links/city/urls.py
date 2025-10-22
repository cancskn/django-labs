from django.urls import path, re_path
from . import views


# urlpatterns = [
#     path('', views.main, name='main'),
#     path('news/', views.news, name='news'),
#     path('administration/', views.administration, name='administration'),
#     path('facts/', views.facts, name='facts'),
#     path('contacts/', views.contacts, name='contacts'),
# ]

# add regex to urls to handle invalid adresses
urlpatterns = [
    re_path(r'^(?:news.*)$', views.news, name='news'),
    re_path(r'^(?:administration.*)$', views.administration, name='administration'),
    re_path(r'^(?:facts.*)$', views.facts, name='facts'),
    re_path(r'^(?:contacts.*)$', views.contacts, name='contacts'),
    re_path(r'^(?:history/people.*)$', views.history_people, name='history_people'),
    re_path(r'^(?:history/photos.*)$', views.history_photos, name='history_photos'),
    re_path(r'^(?:history.*)$', views.history_main, name='history_main'),
    re_path(r'^(?:.*)$', views.main),
    
]