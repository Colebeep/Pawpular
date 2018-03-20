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

class MapPost(models.Model):
    """
    Model representing a map post
    """

class SocialPost(models.Model):
    """
    Model representing a social post
    """


class ServicePost(models.Model):
    """
    Model representing a service post
    """

class User(models.Model):
    """
    Model representing a user.
    """
    signUpDate = models.DateField()
    posts = 
    lname = models.CharField(max_length=45)
    fname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField()
    pets
    friends
    settings = models.CharField()


class Pet(models.Model):
    """
    Model representing a pet.
    """

class Comment(models.Model):
    """
    Model representing a pet.
    """
