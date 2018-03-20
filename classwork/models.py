from django.db import models

# Example model
class ExampleModel(models.Model):
    """
    Model representing a map post
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

# Create your models here.

POST_TYPES = (
  'SOCIAL',
  'SERVICE',
  'MAP'
)

class Post(models.Model):
    """
    Model representing a map post
    """
    type = models.CharField(choices=POST_TYPES)
    createdBy = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    image = '''idk how to do this one'''
    createdOn = models.DateField()
    latitude = models.CharField()
    longitude = models.CharField()
    expiry = models.DateField()
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)
    cost = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()


class User(models.Model):
    """
    Model representing a user.
    """
    signUpDate = models.DateField()
    posts = models.ForeignKey('Post', on_delete=models.CASCADE)
    lname = models.CharField(max_length=45)
    fname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField()
    pets = models.ForeignKey('Pet',on_delete=models.CASCADE)
    friends = models.ForeignKey('User', on_delete=models.CASCADE)
    settings = models.CharField()


class Pet(models.Model):
    """
    Model representing a pet.
    """

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
