from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView
from django.views import View
from django.utils.translation import gettext as _

import redis
import pickle
import telepot

from task_manager import settings
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.tasks.filters import TaskFilter
from task_manager.users.models import Profile


class IndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        tasks = TaskFilter(
            request.GET,
            queryset=Task.objects.all(),
            profile_id=profile.id,
        )
        return render(request, 'tasks/index.html', context={
            # 'tasks': tasks,
            'filter': tasks
        })


class TaskFormCreateView(LoginRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(
            request, 'tasks/create.html', {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            labels = form.cleaned_data['labels']

            instance.author = Profile.objects.get(
                user=self.request.user
            )
            instance.save()
            for label in labels:
                instance.labels.add(label)
            messages.add_message(
                request, messages.SUCCESS, _('Task created successfully')
            )
            if settings.BOT_TOKEN:
                bot = telepot.Bot(token=settings.BOT_TOKEN)
                msg = f"new task '{instance.name}' created"
                bot.sendMessage(chat_id=settings.BOT_CHAT_ID, text=msg)
            return redirect('tasks')
        messages.add_message(
            request, messages.SUCCESS, _('Enter correct data')
        )
        return render(
            request, 'tasks/create.html', {'form': form}
        )


class TaskFormEditView(LoginRequiredMixin, UpdateView):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(
            request, 'tasks/update.html', {'form': form, 'pk': task_id}
        )

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, _('Task updated successfully')
            )
            return redirect('tasks')

        return render(
            request, 'tasks/update.html', {'form': form, 'pk': task_id}
        )


class TaskView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        try:
            if r.get(f'task_{task_id}'):
                task = pickle.loads(r.get(f'task_{task_id}'))
                labels = task.labels.all()
            else:
                task = Task.objects.get(pk=task_id)
                pickled_task = pickle.dumps(task)
                r.set(f'task_{task_id}', pickled_task)
                labels = task.labels.all()
        except redis.ConnectionError:
            task = Task.objects.get(pk=task_id)
            labels = task.labels.all()
        return render(request, 'tasks/show.html', context={
            'task': task,
            'labels': labels,
        })


class TaskFormDeleteView(LoginRequiredMixin, UpdateView):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(
            request,
            'tasks/delete.html',
            {'form': form, 'pk': task_id, 'name': task.name}
        )

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
            messages.add_message(
                request, messages.SUCCESS, _('Task deleted successfully')
            )
        else:
            messages.add_message(
                request, messages.ERROR, _('There are no such task')
            )
        return redirect('tasks')
