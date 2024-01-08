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
        fields = (
            'id',
            'name',
            'description',
            'status',
            'status_name',
            'executor',
            'executor_name',
            'author',
            'author_name',
            'timestamp',
            'labels',
        )

    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    status_name = serializers.SerializerMethodField()
    executor_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    def get_status_name(self, instance):
        return instance.status.name

    def get_executor_name(self, instance):
        return instance.executor.user.username

    def get_author_name(self, instance):
        return instance.author.user.username
