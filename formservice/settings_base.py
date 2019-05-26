# pylint: disable=wildcard-import,unused-wildcard-import,invalid-name
import environ

from .settings import *

env = environ.Env(DEBUG=(bool, False))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# Application definition

PROJECT_APPS = []

INSTALLED_APPS += [
    'django_extensions',
] + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # http://whitenoise.evans.io/en/stable/index.html#quickstart-for-django-apps
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

EMAIL_CONFIG = env.email_url('EMAIL_URL')

vars().update(EMAIL_CONFIG)
