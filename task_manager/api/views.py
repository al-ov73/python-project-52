from rest_framework import generics, viewsets

from task_manager.api.serializers import StatusSerializer, TaskSerializer
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class StatusesView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
