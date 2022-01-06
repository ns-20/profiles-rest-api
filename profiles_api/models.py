from django.db import models
from django.contrib.auth.models import AbstactBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in teh system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=Fales)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] 

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retriev short name of user"""
        return self.name

    def __str__(self):
        """Retrieve string representation of the user"""
        return self.email

