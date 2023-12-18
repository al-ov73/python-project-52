from django.contrib.auth.models import User
from django.test import TestCase

from task_manager.labels.models import Label


class TestLabels(TestCase):

    def test_is_ok_index(self):
        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        User.objects.create_user(**credentials)
        self.client.post('/login/', credentials, follow=True)

        response = self.client.get('/labels/')
        self.assertEquals(response.status_code, 200)

    def test_create_label(self):

        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        User.objects.create_user(**credentials)
        self.client.post('/login/', credentials, follow=True)

        label_data = {
            'name': 'testlabel',
        }
        self.client.post('/labels/create/', label_data)
        label = Label.objects.get(name=label_data['name'])
        self.assertIsInstance(label, Label)

    def test_delete_label(self):
        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        User.objects.create_user(**credentials)
        self.client.post('/login/', credentials, follow=True)

        credentials = {
            'name': 'testlabel',
        }
        self.client.post('/labels/create/', credentials, follow=True)
        label = Label.objects.get(name=credentials['name'])
        pk = label.pk
        self.client.post(f'/labels/{pk}/delete/')
        self.assertFalse(Label.objects.filter(id=pk))
