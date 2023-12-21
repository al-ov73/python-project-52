from django import forms
from django.utils.translation import gettext as _

from task_manager.labels.models import Label


class LabelForm(forms.ModelForm):

    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Label
        fields = ['name']
