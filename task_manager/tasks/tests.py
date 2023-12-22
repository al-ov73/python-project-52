from django.test import TestCase

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.tests import create_and_login_user
from task_manager.users.models import User


class TestTaskes(TestCase):

    fixtures = ["label.json", "status.json"]

    def test_is_ok_index(self):

        create_and_login_user(self)
        response = self.client.get('/tasks/')
        self.assertEquals(response.status_code, 200)

    def test_create_and_delete_task(self):

        create_and_login_user(self)
        user = User.objects.get(username='Testuser')
        status = Status.objects.get(name='status_name')
        label = Label.objects.get(name='label_name')
        task_data = {
            'name': 'task_name',
            'description': 'task_description',
            'status': status.id,
            'labels': label.id,
            'executor': user.id,
        }
        self.client.post('/tasks/create/', task_data, request={'user': user})
        new_task = Task.objects.get(name=task_data['name'])
        self.assertIsInstance(new_task, Task)
        id = new_task.id
        self.client.post(f'/tasks/{id}/delete/')
        self.assertFalse(Task.objects.filter(id=id))
