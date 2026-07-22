![pipeline status](https://gitlab.com/zhenek276/api-pytest-project/badges/main/pipeline.svg)
# API Test Automation Framework


Автоматизированное тестирование REST API на Python с использованием Pytest.

Проект демонстрирует построение API автотестов, работу с CI/CD и интеграцию с системой управления тестированием Qase TestOps.

---

# Stack

- Python
- Pytest
- Requests
- Git
- GitLab CI/CD
- GitLab Runner
- Docker
- Qase TestOps

---

# Tested API

В проекте используется публичный REST API: https://jsonplaceholder.typicode.com


Покрытые endpoints:

Users:

- GET /users
- GET /users/{id}

Posts:

- GET /posts
- GET /posts/{id}
- POST /posts
- PUT /posts/{id}
- PATCH /posts/{id}
- DELETE /posts/{id}

---

# Test Coverage

В проекте реализованы проверки:

- HTTP status codes
- JSON structure validation
- Required fields validation
- Response data validation
- Data types validation
- Nested JSON objects validation
- Empty values validation
- CRUD operations
- Pytest fixtures
- Parametrize tests

---

# Project Structure
api-pytest-project/

├── test/
│ ├── test_users.py
│ └── test_posts.py
│
├── api_client.py
├── config.py
├── conftest.py
│
├── requirements.txt
├── pytest.ini
│
├── Dockerfile
├── .dockerignore
├── .gitignore
│
└── .gitlab-ci.yml





---
## CI/CD

Pipeline runs automatically on GitLab after push.

Features:
- GitLab Runner (Shell executor)
- pytest execution
- Qase TestOps reporting
- Protected CI/CD variables
- Proxy configuration for restricted services

# Project Components

## api_client.py

Содержит функции для выполнения API запросов:

- GET
- POST
- PUT
- PATCH
- DELETE


## config.py

Хранит:

- Base URL
- API endpoints


## conftest.py

Содержит общие pytest fixtures.


## tests

Содержит автоматизированные тесты API.

---

# Running Tests Locally

Install dependencies:

```bash
pip install -r requirements.txt

Run tests: pytest -v

Running Tests with Docker

Build image: docker build -t api-pytest-project .
Run tests: docker run --rm api-pytest-project



CI/CD Pipeline

Автоматический запуск тестов настроен через GitLab CI/CD.

Pipeline flow:


git push
    |
    ↓
GitLab Repository
    |
    ↓
GitLab Pipeline
    |
    ↓
GitLab Runner
    |
    ↓
Pytest
    |
    ↓
Qase TestOps Report

Pipeline выполняет:

Создание виртуального окружения
Установку зависимостей
Запуск автотестов
Отправку результатов в Qase TestOps

Test Management

Проект интегрирован с Qase TestOps.

Используется:

автоматическая отправка результатов тестов
привязка автотестов к test cases
история запусков
отображение Passed / Failed результатов


Author

Evgeniy Stepanenko

API Test Automation Project