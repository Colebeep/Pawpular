from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    """
    abstract representing a any post
    """
    createdBy = models.ForeignKey('User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/',blank = True)
    createdOn = models.DateField()
    title = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class MapPost(Post):
    imageUrl = models.CharField(max_length=1000, default='')
    latitude = models.CharField(max_length=45, default='')
    longitude = models.CharField(max_length=45, default='')
    expiry = models.DateField()
    
class FeedPost(Post):
    """
     -We should also include an optional image field in future
    """
    comments = models.ManyToManyField('Comment', blank=True)
    
class ServicePost(Post):
    cost = models.IntegerField(blank=True)
    startDate = models.DateField()
    endDate = models.DateField()


class User(models.Model):
    """
    Model representing a user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    signUpDate = models.DateField()
    lname = models.CharField(max_length=45)
    fname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    image = models.ImageField(upload_to='uploads/',blank = True)
    #pets = models.ForeignKey('pet',on_delete=models.CASCADE, blank=False)
    password = models.CharField(max_length=45)
    friends = models.ManyToManyField('User', blank=True)
    pets = models.ManyToManyField('Pet', blank=True)
    feedPosts = models.ManyToManyField('FeedPost', blank=True)
    mapPosts = models.ManyToManyField('MapPost', blank=True)
    servicePosts = models.ManyToManyField('ServicePost', blank=True)
    #we need more of these sort of things for the settings page


#this is for the user pointer to the user created in the database. here will store the particulars
# user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    status=(
        ('1','on'),
        ('0','off'),
        )

    settings = models.CharField(max_length=1,choices=status, blank=False,default='1',help_text = 'settings status status')

    def __str__(self):
        return self.lname + ", " + self.fname

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

class Pet(models.Model):
    """
    Model representing a pet.
        -the pet type should be a required field
        -dog
        -cat
        -rabbit
        -... you get the idea

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to='uploads/',blank = True)
    name = models.CharField(max_length=45, blank=False)
    birthday = models.DateField('Birthday', null=True, blank=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    """
    Model representing a comment
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField(max_length=400, help_text="What are your thoughts..")
    user = models.ForeignKey('User',on_delete=models.CASCADE, null=True, blank=False)
    post = models.ManyToManyField('FeedPost', blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id.__str__()
