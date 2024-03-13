# api_yatube
Проект «api_yatube» - это API социальной сети yatube, доступ к постам, комментариям, группам и подпискам Yatubeпредоставляется в зависимости от статуса пользователя. Аутентификация реализована через JWT-токену.

### Список использованных технологий:

Pythob 3.7.9
Django 2.2.16
Django REST framework

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/admi20/pet_poject_Yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

Получить список всех публикаций. 

```
GET /api/v1/posts/
```
Получение публикации по id.

```
GET /api/v1/posts/{id}/
```
Получение комментария к публикации по id.

```
GET /api/v1/posts/{post_id}/comments/{id}/
```
После запуска сервера подробная документация доступна по адресу: 
http://localhost:8000/redoc/