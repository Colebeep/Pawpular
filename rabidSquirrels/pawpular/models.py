from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    createdBy = models.ForeignKey('Profile', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField(max_length=150)
    image = models.ImageField(upload_to='uploads/', blank=True,max_length=100)
    createdOn = models.DateField()
    title = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ["-createdOn","createdBy"]

class MapPost(Post):
    latitude = models.CharField(max_length=45, default='')
    longitude = models.CharField(max_length=45, default='')
    expiry = models.DateField(default='')
    
class FeedPost(Post):
    post = models.TextField(max_length=1000, default='')
    
class ServicePost(Post):
    cost = models.IntegerField(blank=True)
    startDate = models.DateField()
    endDate = models.DateField()


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to='uploads/',blank = True)
    pets = models.ManyToManyField('Pet', blank=True)
    feedPosts = models.ManyToManyField('FeedPost', blank=True)
    mapPosts = models.ManyToManyField('MapPost', blank=True)
    servicePosts = models.ManyToManyField('ServicePost', blank=True)

    status=(
        ('1','on'),
        ('0','off'),
        )

    settings = models.CharField(max_length=1,choices=status, blank=False,default='1',help_text = 'settings status status')

    def __str__(self):
        return self.user.last_name + ", " + self.user.first_name

    def get_absolute_url(self):
        return "/pawpular/profile/" + self.uuid.__str__()

class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to='uploads/',blank = True)
    name = models.CharField(max_length=45)
    birthday = models.DateField('Birthday', null=True, blank=True)
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=False)
    
    class Meta:
        ordering =["name"]
    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField(max_length=400, help_text="What are your thoughts..")
    user = models.ForeignKey('Profile',on_delete=models.CASCADE, null=True, blank=False)
    post = models.ManyToManyField('FeedPost', blank=True)
    
    class Meta:
        ordering=["id"]
    
    def __str__(self):
        return self.id.__str__()
