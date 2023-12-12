from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from task_manager.users.models import User, Profile

class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

# class ProfileForm(UserCreationForm):
#     class Meta:
#
#         model = Profile
#         fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

class ProfileUpdateForm(UserChangeForm):

    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    labels = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'username': 'Имя пользователя',
        'password1': 'Пароль',
        'password2': 'Подтверджение пароля',
    }
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-input'}),
        'surname': forms.TextInput(attrs={'class': 'form-input'}),
        'username': forms.TextInput(attrs={'class': 'form-input'}),
    }

    class Meta:

        model = Profile
        fields = ['name', 'surname', 'username', 'password1', 'password2']