from django.contrib import admin
from .models import MapPost, FeedPost, ServicePost, Profile, Pet, Comment
# Register your models here.
myModels = [MapPost, FeedPost, ServicePost, Profile, Pet, Comment]
admin.site.register(myModels)