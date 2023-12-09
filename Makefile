start:
	python manage.py runserver

test:
	python manage.py test


locale1:
	django-admin makemessages --all

locale2:
	django-admin compilemessages

migrate:
	python manage.py makemigrations
	python manage.py migrate
