from django.urls import path, include

from task_manager.users import views

urlpatterns = [
    path('create/', views.UserFormCreateView.as_view(), name='users_create'),
    path('<int:pk>/update/', views.UserFormEditView.as_view(), name='users_update'),
    path('<int:pk>/delete/', views.UserFormDeleteView.as_view(), name='users_delete'),
    path('', views.IndexView.as_view(), name='users'),
]