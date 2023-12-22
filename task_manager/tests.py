from django.contrib.auth.models import User

from task_manager.users.models import Profile


def create_and_login_user(self):
    credentials = {
        'username': 'Testuser',
        'email': 'test@test.ru',
        'password': 'Testpass123',
    }

    user = User.objects.create_user(**credentials)
    Profile.objects.create(user=user)
    self.client.post('/login/', credentials, follow=True)
    return user
