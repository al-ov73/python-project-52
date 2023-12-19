from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.contrib.auth import logout

from django.contrib.auth import login as auth_login
from task_manager.users.forms import AuthenticationUserForm

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello'] = _('Hello')
        return context


class LoginUser(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        messages.add_message(
            self.request, messages.SUCCESS, 'Вы залогинены'
        )
        return HttpResponseRedirect(self.get_success_url())


def logout_view(request):
    logout(request)
    messages.add_message(
        request, messages.INFO, 'Вы разлогинены'
    )
    return redirect('index')
