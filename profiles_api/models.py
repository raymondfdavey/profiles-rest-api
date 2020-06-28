from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#HERE IS THE MODEL MANAGER FOR THE CUSTOM MODEL BELOW. THIS WAS WRITTE AFFFTTTERR THE MODEL

# when defining a class the BaseUserManager bit in the one below is the parent class

# managers work by soecifying functions which can be used to manipulate objects within the model the manager is for

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    #this specifies what thecommand create_user will do nd what is requires in terms of actual user input. the ValueError bit is what puthon will display if no email is put in
    #in this case it will create and return the user object after saving it into the database(after having done any shit we want to it)
    def create_user(self, email, name, password=None):
        """create a new user profile from inputted details"""
        if not email:
            raise ValueError("User must have an email address")

        #we also need to normalise the email address as the second half of the email is case insensitive. most places gmail etc first half is also case insensitive, but not all.
        email = self.normalise_email(email)
        
        #this next bit creates a new model object called user which has the email set to the email of the model being controlled and the name the same

        user = self.model(email=email, name=name)

        #this next bit uses an inbuilt bit of AbstractBaseUser class to set the password as a hashed version of the inputted password. Basically the set_password function encrypts the password before putting it into the database
        user.set_password(password)
        #here we specify the database to be saved to, using standard django syntax as specified in docs.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        #don't need to specift self below because it is automatically called because it is a class function i.e. part of the same class...its just a python thing
        user = self.create_user(email, name, password)
        user.is_superuser = True
        #is_superuser is created by the PermissionsMixin parent class in the UserProfile bit (ie the DB will have that on it just cos of PermissionsMixin)
        user.is_staff = True
        user.save(using=self._db)

        return user

#This model is just the set up of the database - like the instructions for setting it up = like the architectural plan, or framework. The manager above is what describes how it is the populated by user info

class UserProfile(AbstractBaseUser, PermissionsMixin):
#this string below is the "docstring which tells people about the class"
#this new class allows us the functionality of the default user stuff but with added customiseability
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    #the above code defines the first field in our model/Database
    #this says we want an email column on our user profile database table and we want that column to be an email filed with a max length 255 chars and that it is unique in the system
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #next we need to specify the model manager we are going to use for the objects. we need to use our custom user model with the django cli. Django needs custom model manager for the UserProfile model so it knows how to create users and control users using the django command line tools

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    #We need this because we are replacing the default profile class which has a username field

    #now we will add some functions which django can iteract with our custom user User model

    #this first function will enable django to access the name of the user.
    #we must have the first argument as 'self' as this is a function in a class which is a default python convention. required
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

        #next we have to specify the string representation of our model. its the item we want to return when we convert a user profuile obect to a string in python. recommended for all django models because otherwise when you convert it to a string it wont necessarily be a meaningful output. this allows you to specify what you want to return when you are trying to access it in django admin.


    def ___str___(self):
        """return string representation of our user"""
        return self.email
