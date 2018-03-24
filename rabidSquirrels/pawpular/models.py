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
    test = models.CharField(max_length=150)
    
    
class ServicePost(Post):
    title = models.CharField(max_length=150)
    cost = models.IntegerField(blank=True)
    startDate = models.DateField()
    endDate = models.DateField()


class User(models.Model):
    """
    Model representing a user.
    """
    signUpDate = models.DateField()
    lname = models.CharField(max_length=45)
    fname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    pets = models.ForeignKey('Pet',on_delete=models.CASCADE, blank=True, null=True)
    friends = models.ManyToManyField('User', blank=True)
    settings = models.CharField(max_length=45,default='')


class Pet(models.Model):
    """
    Model representing a pet.
        -the name and owner i think should be required fields

    """

    name = models.CharField(max_length=45, blank=False)
    birthday = models.DateField('Birthday', null=True, blank=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, blank=False)

class Comment(models.Model):
    """
    Model representing a pet. 
        -We should also include image fields for the future
    """


    text = models.TextField(max_length=400, help_text="What are your thoughts..")
    user = models.ForeignKey('User',on_delete=models.CASCADE, null=True, blank=False)


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.text
