from django.contrib.auth.models import User
from django.test import TestCase

from task_manager.labels.models import Label


class TestLabels(TestCase):

    fixtures = ["user.json", "label.json"]

    credentials = {
        'username': 'Testuser',
        'email': 'test@test.ru',
        'password': 'Testpass123',
    }

    label_data = {
        'name': 'label_name',
    }

    def test_is_ok_index(self):

        # User.objects.create_user(**credentials)
        self.client.post('/login/', self.credentials, follow=True)
        response = self.client.get('/labels/')
        self.assertEquals(response.status_code, 200)

    def test_create_label(self):

        # credentials = {
        #     'username': 'Testuser',
        #     'email': 'test@test.ru',
        #     'password': 'Testpass123',
        # }
        # User.objects.create_user(**credentials)
        self.client.post('/login/', self.credentials, follow=True)
        label = Label.objects.get(id=1)
        self.assertIsInstance(label, Label)

    def test_delete_label(self):
        # credentials = {
        #     'username': 'Testuser',
        #     'email': 'test@test.ru',
        #     'password': 'Testpass123',
        # }
        # User.objects.create_user(**credentials)
        self.client.post('/login/', self.credentials, follow=True)


        # self.client.post('/labels/create/', self.label_data, follow=True)
        label = Label.objects.get(id=1)
        pk = label.id
        print(pk)
        print(label)
        self.client.post('/labels/1/delete/')
        print(label)
        self.assertFalse(Label.objects.filter(id=pk))
