## Описание проекта YATUBE API

YATUBE API - онлайн-система, позволяющая постить и читать публикации в 
социальной сети YATUBE, комментировать их, подписываться на авторов.
-------------------------------

## Использованные технологии

* python 3.7
* django 2.2.16
* djangorestframework 3.12.4
* djangorestframework-simplejwt 4.7.2
* djoser 2.1.0
-------------------------------

## Запуск проекта

1. Клонируйте репозиторий и перейдите в него в командной строке
```bash
git clone https://github.com/lmashik/api_final_yatube.git
```

2. Перейдите в директорию
```bash
cd api_final_yatube
```

3. Cоздайте и активируйте виртуальное окружение
```bash
python3 -m venv env
```

* Если у вас Linux/macOS

    ```bash
    source env/bin/activate
    ```

* Если у вас windows

    ```bash
    source env/scripts/activate
    ```

4. Обновите pip до последней версии
```bash
python3 -m pip install --upgrade pip
```

5. Установите зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```

6. Выполните миграции
```bash
python3 manage.py migrate
```

7. Запустите проект
```bash
python3 manage.py runserver
```
-------------------------------

## Access Token

### Получение Access Token
Для получения access_token необходимо отправить POST запрос к эндпоинту 
http://127.0.0.1:8000/api/v1/jwt/create/, пример которого 
приведен ниже:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/jwt/create/\ 
  -u "<username>:<password>"\
```

При успешном завершении запроса вы получите ответ в формате JSON. 
Пример ответ на запрос получения токена:

```json
{
    "refresh": "some_refresh_token",
    "access": "some_access_token"
}
```

### Обновление Access Token
Для получения нового access_token взамен истекшего необходимо отправить 
POST запрос к эндпоинту http://127.0.0.1:8000/api/v1/jwt/refresh/,
пример которого приведен ниже:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/jwt/refresh/\ 
  -d "refresh:<refresh_token>"\
```

Запрос должен содержать параметр **refresh**, полученный при создании 
токена.
-------------------------------

## Запросы и ответы

### Формат запроса
Запрос осуществляется посредством протокола HTTP 1.1 на адрес, 
соответствующий ресурсу. HTTP-запросы должны содержать заголовок:
_Authorization: Bearer <access_token>_

### Формат ответа
Ответ сервиса представляет собой JSON-документ в кодировке UTF-8, 
содержимое зависит от запроса.

Пример ответа в случае успешного выполнения:

_HTTP 1.1 200 OK_
```json
[
    {
        "id": 1,
        "author": "admin",
        "text": "всем привет!",
        "pub_date": "2022-12-09T21:35:13.387579Z",
        "image": null,
        "group": null
    }
]
```
-------------------------------

## Ресурсы

Ресурс - часть системы, с которой можно работать. В YATUBE API 
ресурсами являются: публикации, группы, комментарии, подписки.
У каждого ресурса уникальный URL.

Для получения списка доступных ресурсов выполните GET-запрос 
к корневому URL API:

```bash
curl -X GET https://api.shl.tools/api/v1/\ 
  -H "Authorization: Bearer <access_token>"
```

Ответ:
```json
{
    "posts": "http://127.0.0.1:8000/api/v1/posts/",
    "groups": "http://127.0.0.1:8000/api/v1/groups/",
    "follow": "http://127.0.0.1:8000/api/v1/follow/"
}
```

К этому списку также добавляются комментарии 
http://127.0.0.1:8000/api/v1/posts/<post_id>/comments/.
-------------------------------

## Автор

Мария Лапикова  
mashik_p@mail.ru

