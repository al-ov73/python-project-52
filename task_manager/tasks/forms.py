from django import forms
from django.utils.translation import gettext as _
from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
