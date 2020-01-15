"""
Django settings for ohmyrss project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'this is a secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.31.189',
    'localhost',
    'ohmyrss.com',
    'www.ohmyrss.com',
]

# Application definition

INSTALLED_APPS = [
    'django_crontab',
    'web.apps.WebConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'web.middlewares.StatsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ohmyrss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tmpl')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'ohmyrss.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 20,
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRONJOBS = [
   ('1 6-23 * * *', 'web.cron.update_all_user_feed'),
   ('30 1,12,18 * * *', 'web.cron.update_all_wemp_feed'),
   ('11 3 * * *', 'web.cron.clean_history_data')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/assets/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

AVATAR_DIR = os.path.join(BASE_DIR, "assets", "avatar")

# redis service
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

# for scrapy use db
REDIS_FEED_DB = 0
# for web use db
REDIS_WEB_DB = 1

# page view count, thumb count, open page count
REDIS_VIEW_KEY = 'VIEW/%s'
REDIS_THUMB_KEY = 'THUMB/%s'
REDIS_OPEN_KEY = 'OPEN/%s'

# register user count
REDIS_REG_KEY = 'REG/%s'

# api response time
REDIS_API_KEY = 'API/ALL'
REDIS_API_AVG_KEY = 'API/AVG/%s/%s'
REDIS_API_TOTAL_KEY = 'API/TOTAL/%s/%s'
REDIS_API_COUNT_KEY = 'API/COUNT/%s/%s'

# for dashboard statistics
REDIS_WEEK_KEY = 'WEEK/%s'
REDIS_VISIT_KEY = 'VISIT/%s/%s'
REDIS_UV_ALL_KEY = 'UV/ALL/%s'
REDIS_UV_NEW_KEY = 'UV/NEW/%s'

# http referer
REDIS_REFER_ALL_KEY = 'REFER/ALL'
REDIS_REFER_PV_KEY = 'REFER/%s'
REDIS_REFER_PV_DAY_KEY = 'REFER/%s/%s'

# user subscribe list
REDIS_USER_SUB_KEY = 'SUB/%s'

SENSITIVE_WORDS = ('科学上网', )

# github OAuth
GITHUB_OAUTH_KEY = '4b40da1eb0585bf03dda'
GITHUB_OAUTH_SECRET = 'c985780931b223658064d3218095d916106238d7'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'my_info': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'info.log'),
            'formatter': 'verbose',
            'when': 'D',
            'interval': 1,
            'backupCount': 90,
        },
        'my_warn': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024,
            'filename': os.path.join(BASE_DIR, 'logs', 'warn.log'),
            'formatter': 'verbose',
            'backupCount': 100,
        },
        'my_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'error.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024,
            'backupCount': 100,
        },
        'django_warn': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024,
            'backupCount': 100,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django_warn'],
            'level': 'INFO',
            'propagate': True,
        },
        'web': {
            'handlers': ['console', 'my_info', 'my_warn', 'my_error'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
