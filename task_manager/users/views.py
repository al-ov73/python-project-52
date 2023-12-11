from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.views import View
from task_manager.users.models import User
from task_manager.users.forms import UserForm, UserUpdateForm
from django.contrib.auth import login, authenticate
import logging

logger = logging.getLogger(__name__)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        #users = User.objects.all().order_by('-timestamp',)
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })

class UserFormCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = User(request.POST)
            # user.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Пользователь успешно создан.')
            return redirect('users')
        messages.add_message(request, messages.SUCCESS, 'Введите корректные данные.')
        return render(request, 'users/create.html', {'form': form})


class UserFormEditView(View):


    def get(self, request, *args, **kwargs):
        if not request.user.pk:
            messages.add_message(request, messages.SUCCESS, 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect('login')
        user_id = kwargs.get('pk')
        if request.user.pk != user_id:
            messages.add_message(request, messages.SUCCESS, 'У вас нет прав для изменения другого пользователя.')
            return redirect('users')
        user = User.objects.get(id=user_id)
        form = UserUpdateForm(instance=user)
        return render(request, 'users/update.html', {'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Данные успешно изменены.')
            return redirect('users')

        return render(request, 'users/update.html', {'form': form, 'user_id': user_id})

class UserFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        if user:
            try:
                user.delete()
            except ProtectedError:
                messages.add_message(request, messages.ERROR, 'У пользователя есть задачи.')
                return redirect('users')
        messages.add_message(request, messages.SUCCESS, 'Пользователь успешно удален.')
        return redirect('users')