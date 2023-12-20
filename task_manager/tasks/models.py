from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import Profile


class Task(models.Model):

    name = models.CharField(max_length=200, verbose_name="Имя")
    description = models.CharField(max_length=200, verbose_name="Описание")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    executor = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='executor',
        verbose_name = "Исполнитель",
    )
    author = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='author', verbose_name = "Только свои задачи"
    )
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    labels = models.ManyToManyField(Label, blank=True, verbose_name = "Метки")

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.label_suffix = ''