
# Django Web Project с Новостным Приложением

## Описание
Этот проект представляет собой простое веб-приложение на Django, включающее функционал работы с шаблонами и статическими файлами. Помимо стандартных страниц, таких как главная страница и страница с рецептами, в проект добавлено новое приложение для отображения новостей. Для оформления используется Bootstrap.

## Функционал
- **Главная страница** (`index.html`)
- **Страница рецептов** (`recipes.html`)
- **Новостная страница** (`news.html`), отображающая список новостей с заголовками, авторами и датами публикации.
- **Шаблоны и статические файлы**: настроена работа с шаблонами и статическими файлами (CSS, JS).

## Установка и настройка

1. **Клонирование репозитория**
 
   git clone https://github.com/ваш-username/webDjProject2.git
   cd webDjProject2
  

2. **Установка виртуального окружения**
  
   python -m venv .venv
   source .venv/bin/activate  # Для Linux/MacOS
   .venv\Scripts\activate     # Для Windows
  

3. **Установка зависимостей**
  
   pip install -r requirements.txt
   ```

4. **Запуск миграций**
   
   python manage.py migrate
  

5. **Запуск локального сервера**
   
   python manage.py runserver
   
   Приложение будет доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Структура проекта


webDjProject2/
├── app/
│   ├── templates/           # HTML-шаблоны
│   │   ├── index.html       # Главная страница
│   │   ├── recipes.html     # Страница рецептов
│   │   ├── news.html        # Новостная страница
│   │   └── layout.html      # Базовый шаблон
│   ├── static/              # Статические файлы (CSS, JS)
│   └── views.py             # Вьюхи приложения
├── news/                    # Новое приложение
│   ├── templates/news/      # Шаблоны новостей
│   │   └── news.html        # Шаблон новостной страницы
│   ├── models.py            # Модели данных
│   ├── admin.py             # Настройки админки
│   └── views.py             # Вьюхи для новостей
├─


─ project/
│   ├── settings.py          # Настройки Django
│   ├── urls.py              # Роутинг проекта
│   └── wsgi.py              # WSGI-сервер
├── manage.py                # Основной скрипт для управления проектом
        # Зависимости Python


## Используемые технологии
- **Django 5.1.3** — для Backend разработки.
- **Bootstrap 5.3** — для стилизации интерфейса.

## Вклад
Будем рады вашему вкладу! Открывайте issues и создавайте pull requests.

## Лицензия
Проект доступен под лицензией MIT.

## Новостное приложение

### Шаблон новостей (`news.html`)

{% extends "layout.html" %}
{% block title %}Новостная страница{% endblock %}
{% block content %}
<h1>Новостная страница</h1>

{% for new in news %}
  <div>
    <h3> {{ new.title }} </h3>
    <p><strong>Автор:</strong> {{ new.username }}</p>
    <p><strong>Дата публикации:</strong> {{ new.published_date|date:"d.m.Y H:i" }}</p>
    <p> {{ new.description }} </p>
    <p> {{ new.content }} </p>
  </div>
{% endfor %}
{% endblock %}


### Модель новостей (`models.py`)
from django.db import models

class News(models.Model):
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")
    title = models.CharField(max_length=50, verbose_name="Название новости")
    description = models.CharField(verbose_name="Краткое описание новости", max_length=200)
    content = models.TextField(verbose_name="Новость")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


### Настройки админки (`admin.py`)

from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('username', 'title', 'published_date')
    search_fields = ('title', 'username')
    list_filter = ('published_date',)


Этот проект позволяет легко расширять функционал, добавляя новые страницы и приложения по мере необходимости.