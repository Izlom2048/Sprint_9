# Sprint_9

Автотесты для сервиса «Продуктовый помощник».

## Что внутри
- Selenium + Pytest + Allure
- Page Object Model
- Dockerfile для запуска тестов
- Docker Compose с Selenoid
- GitHub Actions workflow для CI

## Структура
- `pages/` — Page Object классы
- `locators/` — локаторы страниц
- `tests/` — тесты по функциональности
- `data/` — тестовые данные
- `assets/` — файлы для загрузки
- `selenoid/` — конфигурация Selenoid

## Покрытые сценарии
1. Создание аккаунта
2. Авторизация
3. Создание рецепта

## Локальный запуск
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests --alluredir=allure-results
```

## Генерация отчета Allure
```bash
allure generate allure-results -o allure-report --clean
```

## Запуск через Docker Compose
```bash
docker pull selenoid/chrome:128.0
docker compose up --build --abort-on-container-exit --exit-code-from tests
```

## Что останется сделать после загрузки в GitHub
- запушить файлы в репозиторий;
- запустить workflow в GitHub Actions;
- после успешного прогона сохранить скриншот пайплайна;
- при необходимости закоммитить сгенерированный `allure-report`.
