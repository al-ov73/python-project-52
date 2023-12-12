from django import forms
from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'responsible']


    # def __init__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     self.fields['responsible'].label_from_instance = self.label_from_instance
    #
    # @staticmethod
    # def label_from_instance(obj):
    #     return "%s %s" % (obj.name, obj.surname)
