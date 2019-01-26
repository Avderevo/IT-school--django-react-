import datetime
import os
from configurations import Configuration, values
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import dj_database_url
import raven



class Base(Configuration):

    sentry_sdk.init(
        dsn="https://4899eea574ad4f70b4364842ced5266b@sentry.io/1366606",
        integrations=[DjangoIntegration()]
    )

    RAVEN_CONFIG = {
        'dsn': "https://4899eea574ad4f70b4364842ced5266b@sentry.io/1366606",

    }

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'corsheaders',
        'django_extensions',
        'rest_framework',
        'raven.contrib.django.raven_compat',

        'frontend',
        'users',
        'study',
    ]

    MIDDLEWARE = [
        'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
        'corsheaders.middleware.CorsMiddleware',  # -----------!
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

    ]

    ROOT_URLCONF = 'ITS_api.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
            ,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'ITS_api.wsgi.application'

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'ru'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    REACT_APP_DIR = os.path.join(BASE_DIR, 'frontend')

    STATICFILES_DIRS = [
        os.path.join(REACT_APP_DIR, 'build', 'static'),
    ]

    STATIC_URL = '/static/'

    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),

        'DATETIME_FORMAT': "%m/%d/%Y %H:%M:%S",

    }

    CORS_ORIGIN_ALLOW_ALL = True

    API_DIR = os.path.dirname(os.path.abspath(__file__))

    JWT_AUTH = {
        'JWT_VERIFY': True,
        'JWT_VERIFY_EXPIRATION': True,
        'JWT_LEEWAY': 0,
        'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
        'JWT_ALLOW_REFRESH': True,
        'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
        'JWT_AUTH_COOKIE': 'JWT',
        'JWT_RESPONSE_PAYLOAD_HANDLER': 'ITS_api.utils.my_jwt_response_handler',

    }

    USER_EMAIL_ACTIVATION = False

    EMAIL_USE_TLS = True
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_PASSWORD = ''  # my gmail password
    EMAIL_HOST_USER = ''  # my gmail username
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = ''

    RQ_QUEUES = {
        'default': {
            'HOST': 'localhost',
            'PORT': 6379,
            'DB': 0,
            'DEFAULT_TIMEOUT': 360,
        }
    }

    INTERNAL_IPS = '127.0.0.1'




class Dev(Base):

    SECRET_KEY = '9@s0j(3y6nabfs!*9=$ucs1&3jpxuf4x^(-0@j=hmoay9*ya8p'

    DEBUG = True

    INTERNAL_IPS = ('127.0.0.1',)

    DATABASES = values.DatabaseURLValue('sqlite:///db.sqlite3')


class Prod(Base):

    DEBUG = False

    SECRET_KEY = '9@s0j(3y6nabfs!*9=$ucs1&3jpxuf4x^(-0@j=hmoay9*ya8p'

    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

    STATIC_ROOT = os.path.join(Base.BASE_DIR, '/static/')

    DATABASES = values.DatabaseURLValue('postgres://postgres:postgres@db:5432/ITS')

