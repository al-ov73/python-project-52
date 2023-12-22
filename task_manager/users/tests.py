from django.test import TestCase

from task_manager.users.models import User


class TestUser(TestCase):

    create_data = {
        'first_name': 'username',
        'last_name': 'usersurname',
        'username': 'Testuser',
        'password1': 'Testpass123',
        'password2': 'Testpass123',
    }
    login_data = {
        'username': 'Testuser',
        'password': 'Testpass123',
    }

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

        user = User.objects.create_user(**self.login_data)
        self.assertTrue(user.is_active)
        self.assertEqual(user.username, 'Testuser')
        response = self.client.post('/login/', self.login_data, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_register_user(self):

        self.client.post('/users/create/', self.create_data)
        user = User.objects.get(username=self.create_data['username'])
        self.assertIsInstance(user, User)

    def test_delete_user(self):

        self.client.post('/users/create/', self.create_data, follow=True)
        user = User.objects.get(username=self.create_data['username'])
        pk = user.pk
        self.client.post(f'/users/{pk}/delete/')
        self.assertFalse(User.objects.filter(id=pk))
