# webDjProject2

# Django Web Project

Простое веб-приложение на Django с использованием шаблонов и Bootstrap.

## Функционал
- Главная страница (`index.html`)
- Страница рецептов (`recipes.html`)
- Страницы "О нас" и "Контакты" (добавьте при необходимости)
- Настроена работа с шаблонами и статическими файлами.

## Установка и настройка

### 1. Клонирование репозитория

git clone https://github.com/ваш-username/webDjProject2.git
cd webDjProject2
2. Установка виртуального окружения
bash
Копировать код
python -m venv .venv
source .venv/bin/activate  # Для Linux/MacOS
.venv\Scripts\activate     # Для Windows
3. Установка зависимостей
bash
Копировать код
pip install -r requirements.txt
4. Запуск миграций
bash
Копировать код
python manage.py migrate
5. Запуск локального сервера
bash
Копировать код
python manage.py runserver
Приложение будет доступно по адресу: http://127.0.0.1:8000/

Структура проекта
csharp
Копировать код
webDjProject2/
├── app/
│   ├── templates/         # HTML-шаблоны
│   │   ├── index.html     # Главная страница
│   │   ├── recipes.html   # Страница рецептов
│   │   └── layout.html    # Базовый шаблон
│   ├── static/            # Статические файлы (CSS, JS)
│   └── views.py           # Вьюхи приложения
├── project/
│   ├── settings.py        # Настройки Django
│   ├── urls.py            # Роутинг проекта
│   └── wsgi.py            # WSGI-сервер
├── manage.py              # Основной скрипт для управления проектом
└── requirements.txt       # Зависимости Python
Используемые технологии
Django 5.1.3 — Backend
Bootstrap 5.3 — Frontend стили
Вклад
Будем рады вашему вкладу! Открывайте issues и создавайте pull requests.

Лицензия
Проект доступен под лицензией MIT.