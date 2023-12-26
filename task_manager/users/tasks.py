from time import sleep

from django.contrib import messages
from django.core.mail import send_mail

from task_manager import settings
from celery import shared_task


@shared_task()
def send_mail_to_newuser(request, name):
    sleep(5)
    send_mail('Успешная регистрация в Task Manager!',
              f'Спасибо за регистрацию, {name}',
              settings.EMAIL_HOST_USER,
              ['ovechkin.a.u@mail.ru'])

    print('email отправлен')