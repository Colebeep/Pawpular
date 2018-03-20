from django.contrib import admin
from .models import MapPost, User, Pet, Comment

# Register your models here.
myModels = [MapPost, User, Pet, Comment]
admin.site.register(myModels)