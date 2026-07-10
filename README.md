\# API Pytest Project



Учебный проект с API-автотестами на Python.



\## Стек



\* Python

\* pytest

\* requests

\* Docker

\* Git / GitHub



\## Что тестируется



В проекте написаны автотесты для публичного API:



```text

https://jsonplaceholder.typicode.com

```



Проверяются endpoints:



\* `/users`

\* `/posts`



\## Что покрыто тестами



\* Проверка status code

\* Проверка JSON-ключей

\* Проверка списков объектов

\* Проверка вложенных JSON-структур

\* Проверка значений

\* Проверка типов данных

\* GET / POST / PUT / PATCH / DELETE запросы

\* Fixtures

\* Parametrize



\## Структура проекта



```text

api-pytest-project/

├── api\_client.py

├── config.py

├── conftest.py

├── requirements.txt

├── pytest.ini

├── Dockerfile

├── .dockerignore

├── .gitignore

└── test/

&#x20;   ├── test\_posts.py

&#x20;   └── test\_users.py

```



\## Описание файлов



\* `api\_client.py` — функции для API-запросов

\* `config.py` — базовый URL и endpoints

\* `conftest.py` — общие pytest fixtures

\* `test/` — тесты

\* `requirements.txt` — зависимости проекта

\* `pytest.ini` — настройки pytest

\* `Dockerfile` — запуск тестов в Docker

\* `.dockerignore` — исключения для Docker-образа

\* `.gitignore` — исключения для Git



\## Установка зависимостей



```bash

pip install -r requirements.txt

```



\## Запуск тестов локально



```bash

pytest -v

```



\## Запуск тестов в Docker



Сборка образа:



```bash

docker build -t api-pytest-project .

```



Запуск тестов:



```bash

docker run --rm api-pytest-project

```



\## Результат



На текущем этапе в проекте проходит 40 тестов.



```text

40 passed

```

## CI

Tests are automatically run with Jenkins.



