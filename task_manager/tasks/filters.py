import django_filters
from django import forms
from django.utils.translation import gettext as _

from task_manager.tasks.models import Task
from task_manager.users.models import Profile


class TaskFilter(django_filters.FilterSet):

    status = django_filters.AllValuesFilter(
        field_name='status__name',
        # label=mark_safe(f"{_('Status')}<br/>"),
        label=_('Status'),
        label_suffix='',
        widget=forms.Select
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=Profile.objects.all(),
        label_suffix='',
    )

    labels = django_filters.AllValuesFilter(
        field_name='labels__name',
        label=_('Label'),
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
        fields = ['status', 'executor', 'labels', 'author']
        labels = {
            'executor': _('Executor'),
        }
