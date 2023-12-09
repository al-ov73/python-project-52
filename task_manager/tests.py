from django.test import TestCase

from task_manager.users.models import User


class TestTaskManager(TestCase):

    def test_is_ok_index(self):
        response = self.client.get('/users/')
        self.assertEquals(response.status_code, 200)

    def test_is_ok_login(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

    def test_is_ok_usercreate(self):
        response = self.client.get('/users/create/')
        self.assertEquals(response.status_code, 200)

    def test_login_user(self):
        credentials = {
            'username': 'Testuser',
            'email': 'test@test.ru',
            'password': 'Testpass123',
        }
        user = User.objects.create_user(**credentials)
        self.assertTrue(user.is_active)
        self.assertEqual(user.username, 'Testuser')
        response = self.client.post('/login/', credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_register_user(self):
        credentials = {
            'name': 'username',
            'surname': 'usersurname',
            'username': 'Testuser',
            'password1': 'Testpass123',
            'password2': 'Testpass123',
        }
        response = self.client.post('/users/create/', credentials)
        user = User.objects.get(username=credentials['username'])
        self.assertIsInstance(user, User)

    def test_delete_user(self):
        credentials = {
            'name': 'username',
            'surname': 'usersurname',
            'username': 'Testuser',
            'password1': 'Testpass123',
            'password2': 'Testpass123',
        }
        response = self.client.post('/users/create/', credentials, follow=True)
        user = User.objects.get(username=credentials['username'])
        pk = user.pk
        response = self.client.post(f'/users/{pk}/delete/')
        self.assertFalse(User.objects.filter(id=pk))