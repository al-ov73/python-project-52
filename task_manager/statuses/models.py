from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name