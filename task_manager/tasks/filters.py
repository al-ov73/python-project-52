import django_filters
from django import forms

from task_manager.tasks.models import Task
from task_manager.users.models import Profile


class TaskFilter(django_filters.FilterSet):

    status = django_filters.AllValuesFilter(
        field_name='status__name',
        label='Статус',
        label_suffix=''
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=Profile.objects.all(),
        label_suffix='',
    )

    label = django_filters.AllValuesFilter(
        field_name='label__name',
        label='Метка',
        label_suffix='',
    )
    author = django_filters.BooleanFilter(
        field_name='author',
        method='filter_author',
        widget=forms.CheckboxInput(),
        label_suffix='',
    )

    def __init__(self, *args, **kwargs):
        self.profile_id = kwargs.pop('profile_id')
        super(TaskFilter, self).__init__(*args, **kwargs)

    def filter_author(self, queryset, name, value):
        if not value:
            qs = queryset.all()
        else:
            user = Profile.objects.get(id=self.profile_id)
            qs = queryset.filter(author=user)
        return qs

    class Meta:
        model = Task
        # fields = ['status', 'label', 'author']
        fields = ['status', 'executor', 'label', 'author']
        labels = {
            'executor': 'Исполнитель',
        }