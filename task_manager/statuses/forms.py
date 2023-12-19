from django import forms
from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):

    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Status
        fields = ['name']
