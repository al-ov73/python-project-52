from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from task_manager.users.models import Profile
from task_manager.users.forms import ProfileUpdateForm, CreateUserForm
from django.contrib.auth import login, authenticate
import logging

logger = logging.getLogger(__name__)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Profile.objects.all()
        return render(request,
                      'users/index.html',
                      context={'users': users})


class ProfileFormCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(
            request,
            'users/create.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user.id)
            profile.user = user
            profile.save()
            username = request.POST['username']
            password = request.POST['password1']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.add_message(
                request, messages.SUCCESS,
                'Пользователь успешно зарегистрирован'
            )
            return redirect('login')
        messages.add_message(
            request, messages.SUCCESS, 'Введите корректные данные.'
        )
        return render(
            request, 'users/create.html', {'form': form}
        )


class ProfileFormEditView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.pk:
            messages.add_message(
                request,
                messages.SUCCESS,
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect('login')
        user_id = kwargs.get('pk')
        if request.user.pk != user_id:
            messages.add_message(
                request,
                messages.SUCCESS,
                'У вас нет прав для изменения другого пользователя.'
            )
            return redirect('users')
        user = Profile.objects.get(id=user_id)
        form = ProfileUpdateForm(instance=user)
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': user_id}
        )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Profile.objects.get(id=user_id)
        form = ProfileUpdateForm(
            request.POST, instance=user
        )
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Данные успешно изменены.'
            )
            return redirect('users')

        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': user_id}
        )


class ProfileFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Profile.objects.get(id=user_id)
        profile = User.objects.get(id=user_id)
        if user:
            try:
                user.delete()
                profile.delete()
            except ProtectedError:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'У пользователя есть задачи.'
                )
                return redirect('users')
        messages.add_message(
            request, messages.SUCCESS, 'Пользователь успешно удален.'
        )
        return redirect('users')
