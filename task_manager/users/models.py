from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # def __str__(self):
    #     return self.name


# class User(AbstractUser):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     surname = models.CharField(max_length=200, blank=True, null=True)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=20)
#     timestamp = models.DateTimeField(auto_now_add=True, null=True)