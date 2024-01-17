from django.test import TestCase

import time
from selenium import webdriver as wd

from task_manager.labels.models import Label
from task_manager.tests import create_and_login_user

url = "http://127.0.0.1:8000/"

options = wd.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = wd.Chrome(options=options)

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

        browser.get(url)
        time.sleep(1)
        browser.save_screenshot("media/screenshots/1.png")

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
