from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from task_manager import views, settings

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('', views.HomePageView.as_view(), name='index'),
]

if settings.LOCAL_DEBUG:
    print('LOCAL DEBUG!!')
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
