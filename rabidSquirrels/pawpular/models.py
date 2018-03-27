from django.db import models
import uuid

class Post(models.Model):
    """
    Model representing a map post
    """
    createdBy = models.ForeignKey('User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/',blank = True)
    createdOn = models.DateField()
    class Meta:
        abstract = True



class MapPost(Post):
    title = models.CharField(max_length=150, default='')
    latitude = models.CharField(max_length=45, default='')
    longitude = models.CharField(max_length=45, default='')
    expiry = models.DateField()
    
class FeedPost(Post):
    """
     -We should also include an optional image field in future
    """
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
    image = models.ImageField(upload_to='uploads/',blank = True)
    #pets = models.ForeignKey('pet',on_delete=models.CASCADE, blank=False)
    password = models.CharField(max_length=45)
    friends = models.ManyToManyField('User', blank=True)

    #we need more of these sort of things for the settings page
    status=(
        ('1','on'),
        ('0','off'),
        )

    settings = models.CharField(max_length=1,choices=status, blank=False,default='1',help_text = 'settings status status')


class Pet(models.Model):
    """
    Model representing a pet.
        -the pet type should be a required field
        -dog
        -cat
        -rabbit
        -... you get the idea

    """

    image = models.ImageField(upload_to='uploads/',blank = True)
    name = models.CharField(max_length=45, blank=False)
    birthday = models.DateField('Birthday', null=True, blank=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, blank=False)

class Comment(models.Model):
    """
    Model representing a comment
    """

    
    text = models.TextField(max_length=400, help_text="What are your thoughts..")
    user = models.ForeignKey('User',on_delete=models.CASCADE, null=True, blank=False)


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.text
