from django.conf.urls.static import static
from django.urls import path

from task_manager import settings
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
        '<int:pk>/show/',
        views.ProfileShowView.as_view(),
        name='users_show'
    ),
    path(
        '<int:pk>/delete/',
        views.ProfileFormDeleteView.as_view(),
        name='users_delete'),
    path('', views.IndexView.as_view(), name='users'),
]

if settings.LOCAL_DEBUG:
    print('LOCAL DEBUG!!')
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
