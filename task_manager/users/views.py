from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import ProtectedError, Count
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.views import View
from django.conf import settings

from task_manager.tasks.models import Task
from task_manager.users.models import Profile
from task_manager.users.forms import ProfileUpdateForm, CreateUserForm
from django.utils.translation import gettext as _

import logging

from task_manager.users.tasks import send_mail_to_newuser

logger = logging.getLogger(__name__)


class IndexView(View):

    def get(self, request, *args, **kwargs):

        users = (
            Profile.objects.annotate(Count('executor')).order_by(
                "-executor__count")
        )
        return render(request,
                      'users/index.html',
                      context={
                          'users': users,

                      })


class ProfileFormCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(
            request,
            'users/create.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES.get("avatar")
            user = form.save()
            profile = Profile(user.id)
            profile.user = user
            profile.profile_pic = image
            if settings.LOCAL_DEBUG:
                name_mail = (
                    f'{profile.user.first_name} {profile.user.last_name}'
                )
                send_mail_to_newuser.delay(name_mail)
                messages.add_message(
                    request, messages.SUCCESS,
                    'Вам был отправлен Email'
                )
            profile.save()
            messages.add_message(
                request, messages.SUCCESS,
                _('User registered successfully')
            )
            return redirect('login')
        messages.add_message(
            request, messages.SUCCESS, _('Enter correct data')
        )
        return render(
            request, 'users/create.html', {'form': form}
        )


class ProfileShowView(View):

    def get(self, request, *args, **kwargs):
        profile_id = kwargs.get('pk')
        profile = Profile.objects.get(id=profile_id)
        tasks_author = Task.objects.filter(author=profile).count()
        tasks_executed = Task.objects.filter(executor=profile).count()
        return render(
            request,
            'users/show.html',
            {
                'profile': profile,
                'tasks_author': tasks_author,
                'tasks_executed': tasks_executed,
            }
        )


class ProfileFormEditView(UpdateView):

    def get(self, request, *args, **kwargs):
        if not request.user.pk:
            messages.add_message(
                request,
                messages.SUCCESS,
                _('You are not autorized! Please login.')
            )
            return redirect('login')
        user_id = kwargs.get('pk')
        if request.user.pk != user_id:
            messages.add_message(
                request,
                messages.SUCCESS,
                _("You don't have access to update other user")
            )
            return redirect('users')
        user = User.objects.get(id=user_id)
        form = ProfileUpdateForm(instance=user)
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': user_id}
        )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = ProfileUpdateForm(
            request.POST, instance=user
        )
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                _('User updated successfully')
            )
            return redirect('users')

        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': user_id}
        )


class ProfileFormDeleteView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        return render(
            request,
            'users/delete.html',
            {'user': user}
        )

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
                    _('User has tasks')
                )
                return redirect('users')
        messages.add_message(
            request, messages.SUCCESS, _('User deleted successfully')
        )
        return redirect('users')
