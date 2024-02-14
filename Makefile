start:
	python manage.py runserver

test:
	python manage.py test


locale1:
	django-admin makemessages --all

locale2:
	django-admin compilemessages --use-fuzzy

migrate:
	python manage.py makemigrations
	python manage.py migrate

lint:
	poetry run flake8 task_manager

coverage:
	poetry run coverage run --source='.' manage.py test task_manager.tests && poetry run coverage xml

celery:
	python -m celery -A task_manager worker --loglevel=DEBUG

redis-start:
	redis-server

redis-stop:
	sudo server redis-server stop


docker:
	docker compose -f docker-compose.yml up

# docker compose -f docker-compose.yml build
# docker compose -f docker-compose.yml up