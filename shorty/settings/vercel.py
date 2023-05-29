import os

from django.core.exceptions import ImproperlyConfigured

from .base import *

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise ImproperlyConfigured('No secret key set!')

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', "").split(';')
if not ALLOWED_HOSTS:
    raise ImproperlyConfigured('DJANGO_ALLOWED_HOSTS is not set.')

CSRF_TRUSTED_ORIGINS = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS', "").split(';')
if not CSRF_TRUSTED_ORIGINS:
    raise ImproperlyConfigured('DJANGO_CSRF_TRUSTED_ORIGINS is not set.')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('POSTGRES_DATABASE'),
        "USER": os.getenv('POSTGRES_USER'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD'),
        "HOST": os.getenv('POSTGRES_HOST'),
        "PORT": "5432",
    }
}