from django.urls import path

from task_manager.users import views

urlpatterns = [
    path(
        'create/',
        views.ProfileFormCreateView.as_view(),
        name='users_create'
    ),
    path(
        '<int:pk>/update/',
        views.ProfileFormEditView.as_view(),
        name='users_update'
    ),
    path(
        '<int:pk>/delete/',
        views.ProfileFormDeleteView.as_view(),
        name='users_delete'),
    path('', views.IndexView.as_view(), name='users'),
]
