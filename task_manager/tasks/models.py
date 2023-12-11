from django.contrib.auth.models import AbstractUser
from django.db import models

from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT, related_name='responsible')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
