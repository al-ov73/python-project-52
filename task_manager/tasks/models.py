from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import Profile


class Task(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    responsible = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='responsible'
    )
    author = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='author'
    )
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    label = models.ManyToManyField(Label, blank=True)
