from django.urls import path

from task_manager.labels import views

urlpatterns = [
    path('create/', views.LabelFormCreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', views.LabelFormEditView.as_view(), name='label_update'),
    path('<int:pk>/delete/', views.LabelFormDeleteView.as_view(), name='label_delete'),
    path('', views.IndexView.as_view(), name='labels'),
]