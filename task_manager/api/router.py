from django.urls import path

from rest_framework.routers import DefaultRouter

from task_manager.api.views import StatusesView, StatusesUpdateDeleteView, \
    TasksViewSet

router = DefaultRouter(trailing_slash=True)

urlpatterns = router.urls

urlpatterns.extend([
    path('statuses', StatusesView.as_view()),
    path('statuses/<int:pk>', StatusesUpdateDeleteView.as_view()),
    path('tasks', TasksViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('tasks/<int:pk>', TasksViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy',
    })),
])
