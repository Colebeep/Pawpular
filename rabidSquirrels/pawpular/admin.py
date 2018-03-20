from django.contrib import admin
from .models import MapPost, FeedPost, ServicePost, User, Pet, Comment

# Register your models here.
myModels = [MapPost, FeedPost, ServicePost, User, Pet, Comment]
admin.site.register(myModels)