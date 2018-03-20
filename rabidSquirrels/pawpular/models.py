from django.db import models
import uuid

class Post(models.Model):
    """
    Model representing a map post
    """
    createdBy = models.ForeignKey('User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=150)
    #image = models.ImageField(max_length=500)
    createdOn = models.DateField()
    class Meta:
        abstract = True



class MapPost(Post):
    title = models.CharField(max_length=150, default='')
    latitude = models.CharField(max_length=45, default='')
    longitude = models.CharField(max_length=45, default='')
    expiry = models.DateField()
    
class FeedPost(Post):
    test = models.CharField(max_length=150, default='SOME STRING')
    
    
class ServicePost(Post):
    title = models.CharField(max_length=150, default='SOME STRING')
    cost = models.IntegerField(default='SOME STRING')
    startDate = models.DateField(default='SOME STRING')
    endDate = models.DateField(default='SOME STRING')


class User(models.Model):
    """
    Model representing a user.
    """
    signUpDate = models.DateField()
    #MapPosts = models.ForeignKey('MapPost', on_delete=models.CASCADE, default='')
    lname = models.CharField(max_length=45)
    fname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    pets = models.ForeignKey('Pet',on_delete=models.CASCADE)
    friends = models.ManyToManyField('User')
    settings = models.CharField(max_length=45)


class Pet(models.Model):
    """
    Model representing a pet.
    """

    name = models.CharField(max_length=45)
    birthday = models.DateField('Birthday', null=True, blank=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)

class Comment(models.Model):
    """
    Model representing a pet.
    """
    comment = models.TextField(max_length=400, help_text="What are your thoughts..")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.comment
