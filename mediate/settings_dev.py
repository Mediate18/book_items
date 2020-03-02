"""
Django settings for Mediate Catalogues project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see 
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import socket
from mediate.decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]

ADMINS = [
    ('Micha Hulsbosch', 'm.hulsbosch@let.ru.nl')
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'bootstrap3',
    'rest_framework',
    'guardian',
    'django_filters',
    'django_tables2',
    'django_select2',
    'dal',
    'dal_select2',
    'viapy',
    'dbbackup',
    'maintenance_mode',
    'test_without_migrations',
    'simple_history',
    'leaflet',
    'simplemoderation',
    'tagme',
    'mediate',
    'global',
    'items',
    'transcriptions',
    'persons',
    'catalogues',
    'dashboard',
    'registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'mediate.urls'

MAIN_TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = [MAIN_TEMPLATE_DIR]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mediate.context_processors.application_instance_type',
            ],
        },
    },
]

WSGI_APPLICATION = 'mediate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': config('DB_NAME'),
        'TEST': {
            'NAME': config('TEST_DB_NAME', None),
        }
    }
}

print(DATABASES['default']['NAME'])

# Check the availability of Redis at startup
# otherwise use a database cache
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

REDIS_PORT = config('REDIS_PORT', 0, cast=int)

try:
    socket.connect(('127.0.0.1', REDIS_PORT))
    socket.close()
    print("Starting with Redis cache (port: {})".format(REDIS_PORT))
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:{}/1".format(REDIS_PORT),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            },
            "KEY_PREFIX": "mediate",
            "TIMEOUT": 60*60*24  # 24 hours
        }
    }
except ConnectionRefusedError:
    print("Starting with database cache")
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': config('CACHE_LOCATION', default="mediate_cache"),
            'TIMEOUT': 60*60*24  # 24 hours
        }
    }

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console', ],
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'URL_FIELD_NAME': 'api-url'
}

SITE_ID = 1

DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap-responsive.html'

BOOTSTRAP3 = {
    'jquery_url': '//code.jquery.com/jquery-2.x-git.min.js'
}

MODERATED_OBJECT_PK = "use_uuid"
MODERATION_OFF = config('MODERATION_OFF', False, cast=bool)

TAGME_OBJECT_ID_TYPE = "uuid"

APPLICATION_INSTANCE_TYPE = config('APPLICATION_INSTANCE_TYPE', default="")

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/var/backups'}

WRITABLE_FOLDER = os.path.normpath(os.path.join(BASE_DIR, config('WRITABLE_FOLDER')))
MEDIA_ROOT = os.path.join(WRITABLE_FOLDER, 'media')
MEDIA_URL = '/protected_media/'
XSENDFILE = config('XSENDFILE', True, cast=bool)
FILE_UPLOAD_PERMISSIONS = 0o640

# The next bit find all '.*layout.html' files in the main template directory
# and extracts the first parts
LAYOUT_SUFFIX = 'layout.html'
AVAILABLE_LAYOUTS = [
    template[:-len(LAYOUT_SUFFIX)]
    for template in os.listdir(MAIN_TEMPLATE_DIR)
    if template.endswith(LAYOUT_SUFFIX) and os.path.isfile(os.path.join(TEMPLATES[0]['DIRS'][0], template))
]

MAINTENANCE_MODE = config('MAINTENANCE_MODE', False, cast=bool)

TEST_WITHOUT_MIGRATIONS_COMMAND = 'django_nose.management.commands.test.Command'
