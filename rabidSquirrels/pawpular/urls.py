from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),


    path('chat/', views.Chat.as_view(), name='chat'),


    path('map/', views.Map.as_view(), name='map'),
    path('profile/', views.Profile.as_view(), name='profile'),



    path('services/', views.Services.as_view(), name='services'),



    path('settings/', views.settings, name='settings'),
]
