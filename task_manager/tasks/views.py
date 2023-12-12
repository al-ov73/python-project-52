from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import UpdateView, CreateView
from django.views import View

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.users.models import Profile


class IndexView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            tasks = Task.objects.all()

            return render(request, 'tasks/index.html', context={
                'tasks': tasks,
            })
        else:
            return redirect('index')

class TaskFormCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = Profile.objects.get(user=self.request.user)
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Задача успешно создана.')
            return redirect('tasks')
        messages.add_message(request, messages.SUCCESS, 'Введите корректные данные.')
        return render(request, 'tasks/create.html', {'form': form})

class TaskFormEditView(UpdateView):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'tasks/update.html', {'form': form, 'pk': task_id})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Статус успешно изменен.')
            return redirect('tasks')

        return render(request, 'tasks/update.html', {'form': form, 'pk': task_id})

class TaskView(View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(pk=task_id)
        print(task.name)
        return render(request, 'tasks/show.html', context={
            'task': task,
        })

class TaskFormDeleteView(UpdateView):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'tasks/delete.html', {'form': form, 'pk': task_id, 'name': task.name})
    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
        messages.add_message(request, messages.SUCCESS, 'Задача успешно удалена.')
        return redirect('tasks')