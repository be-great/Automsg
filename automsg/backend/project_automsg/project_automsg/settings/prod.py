from project_automsg.settings.base import *


DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_db",
        "USER": "admin",
        "PASSWORD": "1234",
        "HOST": "mysql",
        "PORT": "3306",
    }
}


AUTH_COOKIE_SECURE=True
