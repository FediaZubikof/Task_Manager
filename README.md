# Task_Manager
Менеджер задач созданный с использованием Django. Учебный проект.

# Обзор проекта
1. Регистрация
2. Создание новой задачи.
3. Редактировать\Удалить задачу.
4. Запустить\Остановить таймер выполнения задачи.
5. Изменить\Обновить статус задачи.
6. Прикрепите фото к заданию (по необходимости).

# Установка и настройка
Чтобы запустить проект локально, выполните следующие действия:
1. Клонируем репозиторий:
git clone https://github.com/FediaZubikof/Task_Manager.git

2. Перейти в каталог taskManager
cd task_manager

3. Установить зависимости, выполнить миграции в базу данных, запустить сервер разработки.
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

4. Открыть проект в своем веб-браузере: http://127.0.0.1:8000/.

# API Endpoint

Получить все входные значения

Список всех задач: GET http://127.0.0.1:8000/api/task/

Создать задачу: POST http://127.0.0.1:8000/api/task/

In Body:  

{
  "user": 1,
  
  "title": "Тест на API",
  
  "description": "Пробная задача на API",
  
  "d_time": "2024-02-28",
  
  "priority": "Высокий"
}


Получить задачу: GET http://127.0.0.1:8000/api/task/{task_id}/

Обновить задачу: PUT or PATCH http://127.0.0.1:8000/api/task/{task_id}/

In Body:

{
  "id": 33,
  "user": 1,
  "title": "Привет",
  "description": "Пробная с PUT",

  "d_time": "2024-02-28T12:13:14Z",
  "priority": "Низкий",
  "mark": false
  }


Удалить задачу: DELETE http://127.0.0.1:8000/api/task/{task_id}/
