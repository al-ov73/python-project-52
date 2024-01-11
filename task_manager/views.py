from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from django.contrib.auth import login as auth_login

import telepot

from task_manager import settings
from task_manager.tasks.models import Task
from task_manager.users.forms import AuthenticationUserForm
from task_manager.users.models import Profile


class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if settings.BOT_TOKEN:
            bot = telepot.Bot(token=settings.BOT_TOKEN)
            msg = "Someone came to your site"
            bot.sendMessage(chat_id=settings.BOT_CHAT_ID, text=msg)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_users = Profile.objects.count()
        context['users'] = total_users
        context['tasks'] = Task.objects.count()
        tasks = Task.objects.all()
        users = set()
        for task in tasks:
            users.add(task.executor)
        context['free_users'] = total_users - len(users)
        return context


class LoginUser(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        messages.add_message(
            self.request, messages.SUCCESS, _('You are logged in')
        )
        return HttpResponseRedirect(self.get_success_url())


def logout_view(request):
    logout(request)
    messages.add_message(
        request, messages.INFO, _('You are logged out')
    )
    return redirect('index')
