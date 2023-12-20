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

lint:
	poetry run flake8 task_manager

coverage:
	poetry run coverage run --source='.' manage.py test task_manager.tests && poetry run coverage xml