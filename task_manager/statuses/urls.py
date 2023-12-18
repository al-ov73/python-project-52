from django.urls import path

from task_manager.statuses import views

urlpatterns = [
    path(
        'create/',
        views.StatusFormCreateView.as_view(),
        name='status_create'
    ),
    path(
        '<int:pk>/update/',
        views.StatusFormEditView.as_view(),
        name='status_update'
    ),
    path(
        '<int:pk>/delete/',
        views.StatusFormDeleteView.as_view(),
        name='status_delete'
    ),
    path('', views.IndexView.as_view(), name='statuses'),
]
