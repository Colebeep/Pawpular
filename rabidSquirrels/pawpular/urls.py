from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('map/', views.map, name='map'),
    path('profile/', views.profile, name='profile'),
    path('services/', views.services, name='services'),
    path('settings/', views.settings, name='settings'),
]
