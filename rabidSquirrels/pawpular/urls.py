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
    path('profile/<uuid:pk>', views.profile_detail_view.as_view(), name='profile'),


    path('create_service/', views.ServiceCreate.as_view(), name='service_create'),

    #these pageds do not it should tho. every user has their own security settings.
    path('settings/', views.settings, name='settings'),
    path('map/mappost/new',views.mappost_new, name='mappost_new'),
    path('chat/feedpost/new',views.feedpost_new, name='feedpost_new')

] + static('uploads/', document_root=settings.MEDIA_ROOT)

    
