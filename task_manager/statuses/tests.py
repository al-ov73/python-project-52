from django.test import TestCase

from task_manager.statuses.models import Status

class TestStatuses(TestCase):

    def test_is_ok_index(self):
        response = self.client.get('/statuses/')
        self.assertEquals(response.status_code, 200)

    def test_create_status(self):
        credentials = {
            'name': 'teststatus',
        }
        response = self.client.post('/statuses/create/', credentials)
        status = Status.objects.get(name=credentials['name'])
        self.assertIsInstance(status, Status)

    def test_delete_user(self):
        credentials = {
            'name': 'teststatus',
        }
        response = self.client.post('/statuses/create/', credentials, follow=True)
        status = Status.objects.get(name=credentials['name'])
        pk = status.pk
        response = self.client.post(f'/statuses/{pk}/delete/')
        self.assertFalse(Status.objects.filter(id=pk))
