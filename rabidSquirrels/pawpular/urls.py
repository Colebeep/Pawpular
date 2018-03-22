from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.chat, name='chat'),
    path('', views.map, name='map'),
    path('', views.profile, name='profile'),
    path('', views.services, name='services'),
    path('', views.settings, name='settings'),
]
