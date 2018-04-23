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
    path('chat/feedpost/new',views.feedpost_new, name='feedpost_new'),
    path(r'chat/feedpost/edit/<id>', views.feedpost_edit, name='feedpost_edit'),

    path('profile/create_pet', views.pet_new, name = "pet_create")

] + static('uploads/', document_root=settings.MEDIA_ROOT)