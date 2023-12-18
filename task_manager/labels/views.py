from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView
from django.views import View

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label


class IndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels/index.html', context={
            'labels': labels,
        })


class LabelFormCreateView(LoginRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):
        form = LabelForm()
        return render(request, 'labels/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Метка успешно создана.'
            )
            return redirect('labels')
        messages.add_message(
            request, messages.SUCCESS, 'Введите корректные данные.'
        )
        return render(
            request, 'labels/create.html', {'form': form}
        )


class LabelFormEditView(LoginRequiredMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = LabelForm(instance=label)
        return render(
            request,
            'labels/update.html',
            {'form': form, 'pk': label_id}
        )

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = LabelForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Статус успешно изменен.'
            )
            return redirect('labels')

        return render(
            request,
            'labels/update.html',
            {'form': form, 'pk': label_id}
        )


class LabelFormDeleteView(LoginRequiredMixin, UpdateView):

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = LabelForm(instance=label)
        return render(
            request,
            'labels/delete.html',
            {'form': form, 'pk': label_id, 'name': label.name}
        )

    def post(self, request, *args, **kwargs):

        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        if label.task_set.exists():
            messages.add_message(
                request,
                messages.ERROR,
                f'Невозможно удалить метку \
                {label.name}. Есть задачи с этой меткой.'
            )
            return redirect('labels')
        if label:
            label.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Метка успешно удалена.'
        )
        return redirect('labels')
