from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),


    path('chat/', views.Chat.as_view(), name='chat'),


    path('map/', views.map, name='map'),
    path('profile/', views.profile, name='profile'),



    path('services/', views.Services.as_view(), name='services'),



    path('settings/', views.settings, name='settings'),
]
