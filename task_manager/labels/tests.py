from django.test import TestCase

from task_manager.labels.models import Label
from task_manager.tests import create_and_login_user


class TestLabels(TestCase):

    label_data = {
        'name': 'label_name',
    }
    updated_label_data = {
        'name': 'updated_name',
    }

    def test_is_ok_index(self):

        create_and_login_user(self)
        response = self.client.get('/labels/')
        self.assertEquals(response.status_code, 200)

    def test_create_label(self):

        create_and_login_user(self)
        self.client.post('/labels/create/', self.label_data, follow=True)
        label = Label.objects.get(name=self.label_data['name'])
        self.assertIsInstance(label, Label)
        response = self.client.get(f'/labels/{label.id}/update/', follow=True)
        self.assertContains(
            response, self.label_data['name'], status_code=200
        )

    def test_update_label(self):

        create_and_login_user(self)
        self.client.post('/labels/create/', self.label_data, follow=True)
        label = Label.objects.get(name=self.label_data['name'])
        response = self.client.get(f'/labels/{label.id}/update/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.client.post(
            f'/labels/{label.id}/update/', self.updated_label_data, follow=True
        )
        self.assertFalse(Label.objects.filter(name=self.label_data['name']))
        self.assertTrue(
            Label.objects.filter(name=self.updated_label_data['name'])
        )
        response = self.client.get(f'/labels/{label.id}/update/',
                                   follow=True)
        self.assertContains(response, self.updated_label_data['name'],
                            status_code=200)

    def test_delete_label(self):

        create_and_login_user(self)
        self.client.post('/labels/create/', self.label_data, follow=True)
        label = Label.objects.get(name='label_name')
        pk = label.id
        self.client.post(f'/labels/{pk}/delete/')
        self.assertFalse(Label.objects.filter(name='label_name'))
