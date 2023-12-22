from django.test import TestCase

from task_manager.statuses.models import Status
from task_manager.tests import create_and_login_user


class TestStatuses(TestCase):

    status_data = {
        'name': 'teststatus',
    }

    def test_is_ok_index(self):
        create_and_login_user(self)
        response = self.client.get('/statuses/')
        self.assertEquals(response.status_code, 200)

    def test_create_status(self):

        create_and_login_user(self)
        self.client.post('/statuses/create/', self.status_data)
        status = Status.objects.get(name=self.status_data['name'])
        self.assertIsInstance(status, Status)

    def test_delete_status(self):

        create_and_login_user(self)
        self.client.post(
            '/statuses/create/', self.status_data, follow=True
        )
        status = Status.objects.get(name=self.status_data['name'])
        pk = status.pk
        self.client.post(f'/statuses/{pk}/delete/')
        self.assertFalse(Status.objects.filter(name=self.status_data['name']))
