from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView
from django.views import View

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class IndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(
            request,
            'statuses/index.html',
            context={
                'statuses': statuses,
            }
        )


class StatusFormCreateView(LoginRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(
            request,
            'statuses/create.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Статус успешно создан'
            )
            return redirect('statuses')
        messages.add_message(
            request,
            messages.SUCCESS,
            'Введите корректные данные'
        )
        return render(
            request,
            'statuses/create.html',
            {'form': form}
        )


class StatusFormEditView(LoginRequiredMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = StatusForm(instance=status)
        return render(
            request,
            'statuses/update.html',
            {'form': form, 'pk': status_id}
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Статус успешно изменен'
            )
            return redirect('statuses')

        return render(
            request,
            'statuses/update.html',
            {'form': form, 'pk': status_id}
        )


class StatusFormDeleteView(LoginRequiredMixin, UpdateView):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = StatusForm(instance=status)
        return render(
            request,
            'statuses/delete.html',
            {'form': form, 'pk': status_id, 'name': status.name}
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        if status:
            status.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Статус успешно удален'
        )
        return redirect('statuses')
