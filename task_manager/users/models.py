from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    # first_name = models.CharField(max_length=200, blank=True, null=True)
    # last_name = models.CharField(max_length=200, blank=True, null=True)
    # username = models.CharField(max_length=200)
    # password1 = models.CharField(max_length=20)
    # timestamp = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.user.username


# class User(AbstractUser):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     surname = models.CharField(max_length=200, blank=True, null=True)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=20)
#     timestamp = models.DateTimeField(auto_now_add=True, null=True)