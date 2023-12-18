from django.contrib.auth.models import User
from django.test import TestCase

from task_manager.statuses.models import Status


class TestStatuses(TestCase):

    def test_is_ok_index(self):
        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        User.objects.create_user(**credentials)
        self.client.post('/login/', credentials, follow=True)

        response = self.client.get('/statuses/')
        self.assertEquals(response.status_code, 200)

    def test_create_status(self):

        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        User.objects.create_user(**credentials)
        self.client.post('/login/', credentials, follow=True)

        status_data = {
            'name': 'teststatus',
        }
        self.client.post('/statuses/create/', status_data)
        status = Status.objects.get(name=status_data['name'])
        self.assertIsInstance(status, Status)

    def test_delete_status(self):
        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        User.objects.create_user(**credentials)
        self.client.post('/login/', credentials, follow=True)

        credentials = {
            'name': 'teststatus',
        }
        self.client.post(
            '/statuses/create/', credentials, follow=True
        )
        status = Status.objects.get(name=credentials['name'])
        pk = status.pk
        self.client.post(f'/statuses/{pk}/delete/')
        self.assertFalse(Status.objects.filter(id=pk))
