from django.contrib import admin
from pawpular.models import Post, User, Pet, Comment

# Register your models here.
myModels = [Post, User, Pet, Comment]
admin.site.register(myModels)