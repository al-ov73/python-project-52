### Hexlet tests and linter status:
[![Actions Status](https://github.com/al-ov73/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/al-ov73/python-project-52/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/44f2b9a62bd0ac7f774b/maintainability)](https://codeclimate.com/github/al-ov73/python-project-52/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/44f2b9a62bd0ac7f774b/test_coverage)](https://codeclimate.com/github/al-ov73/python-project-52/test_coverage)

4 проект обучения на Hexlet: <br/>
Менеджер задач

https://task-manager-a32f.onrender.com/

Задачам можно присваивать статусы и метки, назначать ответственных.

Во время проекта использовалась база данных PostgreSQL.<br/>
Реализованы тесты Django-Unittest.

Веб-приложение подключено к коллектору ошибок 
<a href="https://rollbar.com/">Rollbar</a>

Чтобы локально запустить проект через **Poetry**, выполните следующие команды:
```commandline
git clone git@github.com:al-ov73/python-project-52.git
cd python-project-52
```
Создайте в корневой директории файл .env со следующими переменными и присвойте им значения
```commandline
DATABASE_URL=
SECRET_KEY=
DJANGO_LOG_LEVEL=
ROLLBAR_ACCESS_TOKEN=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
BOT_TOKEN=
BOT_CHAT_ID=
```
далее введите следующие команды:
```
poetry shell
poetry install
make start
```
Запуск через **Docker**
```commandline
docker pull alov73/task_manager:latest
docker run -p 8000:8000 alov73/task_manager:latest
```