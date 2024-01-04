from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/profile/"
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
