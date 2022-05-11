from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('contact/', views.contact, name='contact.html'),
    path('destinations/', views.destinations, name='destinations.html'),
    path('elements/', views.elements, name='elements.html'),
    path('news/', views.news, name='news.html'),
    path('about/', views.about, name='about.html')
    ]