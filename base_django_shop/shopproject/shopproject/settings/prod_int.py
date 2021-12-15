# подключение к бд в рамках системы контейнеров

from .prod import *

SITE_ID = 1

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'arduinum',
        'PASSWORD': 'geek',
        'HOST': 'db',
        'PORT': '5432'
    }
}
