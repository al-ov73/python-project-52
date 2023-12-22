from django.contrib.auth.models import User


def create_and_login_user(self):
    credentials = {
        'username': 'Testuser',
        'email': 'test@test.ru',
        'password': 'Testpass123',
    }

    User.objects.create_user(**credentials)
    self.client.post('/login/', credentials, follow=True)
