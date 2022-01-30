python -m venv venv  |  добавление виртуального окружения в папку
venv\Scripts\activate.bat  | активация виртуального окружения
pip install django | Установка библиотеки django
django-admin startproject blog | Создаем новый проект Blog
cd blog | переходим в папку blog
python manage.py startapp news | создаем приложение News 
python manage.py migrate | Делаем первые миграции в базу данных SQLlite
python manage.py createsuperuser | Создаем Администратора для нашего сайта

Username: Логин (Admin)
Email address: Почта
Password: Пароль 
Password (again): Повторить пороль
password validation and create user anyway? [y/N]: y (Нажать Y)
Superuser created successfully.

python manage.py runserver |  Запуск сервера

http://127.0.0.1:8000/    |   Адрес Нашего сайта
http://127.0.0.1:8000/admin    |  Админ панель нашего сайта (нужно вводить логин и пароль которые мы создали)

Дом задание
Открываешь модель и пишишь там модели с фото.
Открываешь admin.py и пишешь там свой код с фото
Открываешь settings.py и добовляешь там свой код с фото
В терменале пишешь команду
	1. /venv/Script/activation.bat
	2. cd news
	3. python manage.py makemigrations
	4. python manage.py migrate
