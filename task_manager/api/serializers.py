from rest_framework import serializers

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
