from django import forms
from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):

    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea
    )
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
