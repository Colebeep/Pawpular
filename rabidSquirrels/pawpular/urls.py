from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),

    #these pages have data going into them
    path('chat/', views.Chat.as_view(), name='chat'),
    path('map/', views.Map.as_view(), name='map'),
    path('services/', views.Services.as_view(), name='services'),
    path('profile/<uuid:pk>', views.Profile.as_view(), name='profile'),

    #these pageds do not.
    path('settings/', views.settings, name='settings'),
] + static('uploads/', document_root=settings.MEDIA_ROOT)
