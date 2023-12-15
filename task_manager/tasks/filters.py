import django_filters
from django_filters import rest_framework as filters

from task_manager.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    label = django_filters.AllValuesFilter(field_name='label__name')

    class Meta:
        model = Task
        fields = ['status', 'responsible', 'label']

    # @property
    # def field(self):
    #     self.extra['label'] = [(a.city, a.city) for a in self.parent.queryset]
    #     return super(CityFilter, self).field

    # @property
    # def qs(self):
    #     parent = super().qs
    #     author = getattr(self.request, 'user', None)
    #
    #     return parent.filter(is_published=True) \
    #         | parent.filter(author=author)