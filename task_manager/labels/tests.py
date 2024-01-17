import os
from django.test import TestCase

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


from task_manager.labels.models import Label
from task_manager.tests import create_and_login_user


class TestLabels(TestCase):

    label_data = {
        'name': 'label_name',
    }
    updated_label_data = {
        'name': 'updated_name',
    }

    def test_ui_with_selenium(self):

        url = "http://127.0.0.1:8000/"

        options = wd.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        browser = wd.Chrome(options=options)

        browser.get(url)
        assert "Метки" not in browser.page_source
        enter_button = browser.find_element(By.LINK_TEXT, "Вход")
        enter_button.click()
        login_input = browser.find_element(By.NAME, "username")
        login_input.send_keys(os.getenv('USERNAME'))
        pass_input = browser.find_element(By.NAME, "password")
        pass_input.send_keys(os.getenv('PASSWORD'))
        login_button = browser.find_element(
            locate_with(By.TAG_NAME, "button").below(pass_input))
        login_button.click()
        label_button = browser.find_element(By.LINK_TEXT, "Метки")
        label_button.click()
        label_button = browser.find_element(By.LINK_TEXT, "Создать метку")
        label_button.click()
        label_input = browser.find_element(By.NAME, "name")
        label_input.send_keys('testlabel')
        label_button = browser.find_element(By.CSS_SELECTOR,
                                            '[value="Создать"]')
        label_button.click()
        browser.save_screenshot("media/screenshots/create_label.png")
        assert "testlabel" in browser.page_source
        assert "Метка успешно создана" in browser.page_source
        new_label = browser.find_element(By.XPATH,
                                         "//*[ text() = 'testlabel' ]")
        button = browser.find_element(
            locate_with(By.CSS_SELECTOR, '[value="Удалить"]').to_right_of(
                new_label))
        button.click()
        browser.save_screenshot("media/screenshots/delete_conf_label.png")
        del_button = browser.find_element(By.CSS_SELECTOR,
                                          '[value="Да, удалить"]')
        del_button.click()
        assert "testlabel" not in browser.page_source

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
