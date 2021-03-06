# IT-school--django-react-

### This is a hybrid of Django Rest Api and React Spa applications.

## Install

1 Clone a project :
 ```
 $ git clone https://github.com/Avderevo/IT-school-on-the-React
  ```

2 Installing dependencies:
 ```
 $ pip3 install requirements.txt 
  ```

3 Run the configuration:
 ```
 $ export DJANGO_CONFIGURATION=Dev
 ```
 
4 Starting migrations:
```
$ python manage.py makemigrations users study
$ python manage.py migrate
```
 
5 Set the initial data:
```
$ python manage.py loaddata course.json lessons.json

``` 

6 Run project:
```
$ python manage.py runserver
```

### Что есть ?

На данном этапе проекта есть готовые:

- Главная страница
- Страницы курсов
- Страница тестирования на курс
- Регистрация и вход для студента и преподователя
- Личный кабинет студента
- Личный кабинет преподователя


### Как это работает ?

- ### Для студента:
 - Нажимаем кнопку "логин или регистрация"
 - Регестрируемся в качестве студента и входим
 - Появится кнопка входа в личный кабинет - там пока пусто
 - Для зачисления на курс входим на страницу курса, и нажимаем кнопку "Поступить на курс"
 - Успешно проходим тест и курс появится в личном кабинете
 - Входим на курс
 - В чате карточки курса после отправки сообщения автоматически сообщения не отображаются ( нужно перегружать руками)


- ### Для преподователя
- Нажимаем кнопку "логин/регистрация"
- Регестрируемся в качестве преподователя и входим
- После входа появится кнопка входа в личный кабинет учителя
- Заходим в личный кабинет
- Выбераем курс и регистрируемся на нам в качестве преподователя (курс появится в личном кабинете)
- Входим на курс (Есле на курсе есть зарегестрированные студенты - они появятся в списке студентов)
- В чате, карточка курса после отправки сообщения или смены статуса домашнего задания  автоматически не обновляется (пока нужно перегружать руками)- ищу решения.


### Run Docker:
```
$ docker-compose build
$ docker-compose up

```


### Run tests:

```
$ pytest

```

# Logging in Sentry

#### To customize logging in Sentry change your Configure URL in the  settings.py

```
  sentry_sdk.init(
        dsn="https://4899eea574ad4f70b4364842ced5266b@sentry.io/1366606",
        integrations=[DjangoIntegration()]
    )

    RAVEN_CONFIG = {
        'dsn': "https://4899eea574ad4f70b4364842ced5266b@sentry.io/1366606",

    }

```

### Logging screenshots:

![alt text](https://github.com/Avderevo/IT-school--django-react-/blob/master/img/1.png)

<hr>

![alt text](https://github.com/Avderevo/IT-school--django-react-/blob/master/img/2.png)

<hr>

![alt text](https://github.com/Avderevo/IT-school--django-react-/blob/master/img/3.png)

<hr>

![alt text](https://github.com/Avderevo/IT-school--django-react-/blob/master/img/4.png)