from django.urls import path

from task_manager.tasks import views

urlpatterns = [
    path('create/', views.TaskFormCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', views.TaskFormEditView.as_view(), name='task_update'),
    path('<int:pk>/', views.TaskView.as_view(), name='task_show'),
    path('<int:pk>/delete/', views.TaskFormDeleteView.as_view(), name='task_delete'),
    path('', views.IndexView.as_view(), name='tasks'),
]