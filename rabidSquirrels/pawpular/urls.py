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


    path('services/new/', views.create_new_service, name='service_create'),

    #these pageds do not it should tho. every user has their own security settings.
    path('settings/', views.settings, name='settings'),
    path(r'map/mappost/new/<lat>/<lon>',views.mappost_new, name='mappost_new'),
    path(r'map/mappost/edit/<uuid:pk>',views.mappost_edit.as_view(),name='mappost_edit'),
    path(r'map/mappost/delete/<uuid:pk>',views.mappost_delete.as_view(),name='mappost_delete'),
    
    path('chat/feedpost/new',views.feedpost_new, name='feedpost_new'),
    path(r'chat/feedpost/edit/<uuid:pk>', views.feedpost_edit.as_view(), name='feedpost_edit'),
    path(r'chat/feedpost/delete/<uuid:pk>',views.feedpost_delete.as_view(),name='feedpost_delete'),

    path('profile/create_pet', views.pet_new, name = "pet_create")

] + static('uploads/', document_root=settings.MEDIA_ROOT)