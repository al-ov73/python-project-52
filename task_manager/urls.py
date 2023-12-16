from django.contrib import admin
from django.urls import path, include
from task_manager import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('admin/', admin.site.urls, name='admin'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('', views.HomePageView.as_view(), name='index'),
]
#
# handler404 = 'task_manager.views.error_404'
