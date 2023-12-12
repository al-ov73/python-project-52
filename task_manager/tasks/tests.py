from django.test import TestCase

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TestTaskes(TestCase):

    def test_is_ok_index(self):

        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        user = User.objects.create_user(**credentials)
        response = self.client.post('/login/', credentials, follow=True)
        response = self.client.get('/tasks/')
        self.assertEquals(response.status_code, 200)

    def test_create_task(self):
        user_data = {
            'name': 'username',
            'surname': 'usersurname',
            'username': 'Testuser',
            'password1': 'Testpass123',
            'password2': 'Testpass123',
        }
        self.client.post('/users/create/', user_data)
        user = User.objects.get(username=user_data['username'])

        credentials = {
            'username': 'Testuser',
            'password': 'Testpass123',
        }
        response = self.client.post('/login/', credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        status_data = {
            'name': 'teststatus',
        }
        self.client.post('/statuses/create/', status_data)
        status = Status.objects.get(name=status_data['name'])

        task_data = {
            'name': 'task_name',
            'description': 'task_description',
            'status': status.id,
            'responsible': user.id,
        }
        self.client.post('/tasks/create/', task_data, request={'user': user,})
        new_task = Task.objects.get(name=task_data['name'])
        self.assertIsInstance(new_task, Task)

    # def test_delete_user(self):
    #     credentials = {
    #         'name': 'testtask',
    #     }
    #     response = self.client.post('/tasks/create/', credentials, follow=True)
    #     task = Task.objects.get(name=credentials['name'])
    #     pk = task.pk
    #     response = self.client.post(f'/tasks/{pk}/delete/')
    #     self.assertFalse(Task.objects.filter(id=pk))
