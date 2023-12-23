from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm
)
from django.utils.translation import gettext as _

from task_manager.users.models import User


class AuthenticationUserForm(AuthenticationForm):

    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'placeholder': _('Username')})
    )

    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': _('Password'),
                   "autocomplete": "current-password"}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:

        model = User
        fields = [
            'username',
            'password',
        ]


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]


class ProfileUpdateForm(UserChangeForm):

    first_name = forms.CharField(
        label=_('Name'), widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    last_name = forms.CharField(
        label=_('Surname'),
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-input'}),
        'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        'username': forms.TextInput(attrs={'class': 'form-input'}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:

        model = User
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2'
        ]
