import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import django_heroku
import logging
from decouple import config


# Load environment variables from .env file
load_dotenv()



# Access token from environment variable
INSTAGRAM_ACCESS_TOKEN = config('INSTAGRAM_ACCESS_TOKEN', default='default_local_value')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

import logging

logger = logging.getLogger(__name__)

USE_AWS = os.getenv('USE_AWS', 'False') == 'True'
DEBUG = os.getenv('DEBUG', 'True') == 'True'

if USE_AWS:
    logger.debug("Using AWS S3 for storage.")
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')

    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
    MEDIA_URL = os.getenv('CLOUDFRONT_URL', f"https://{AWS_S3_CUSTOM_DOMAIN}/")

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    
    S3_BASE_URL = os.getenv('CLOUDFRONT_URL', MEDIA_URL)
    logger.debug(f"S3_BASE_URL set to: {S3_BASE_URL}")
else:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / "assets",
    ]
    STATIC_ROOT = BASE_DIR / "staticfiles"

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

    S3_BASE_URL = STATIC_URL

# TEMPLATES setting
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ]
        },
    },
]

# Set DEBUG based on environment
DEBUG = os.getenv('DEBUG', 'True') == 'True'

CRISPY_TEMPLATE_PACK = "bootstrap4"
SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'www.nagswithnotions.ie',
    'nagswithnotions.ie',
    'nags-with-notions-f8a098968cba.herokuapp.com',
]

INSTALLED_APPS = [
    "pizza_system.apps.PizzaSystemConfig",
    "booking.apps.BookingConfig",
    "nags_with_notions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "phonenumber_field",
    "django_summernote",
    "events",
    "widget_tweaks",
    "crispy_forms",
    "crispy_bootstrap4",
    "storages",
    "insta",
]

SITE_ID = 1
LOGIN_URL = "login"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "nags_with_notions.urls"

WSGI_APPLICATION = "nags_with_notions.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv('DATABASE_URL'), conn_max_age=600, ssl_require=True
    )
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeanyapp.com",
    "https://*.herokuapp.com",
    "https://nags-with-notions-f8a098968cba.herokuapp.com",
    "https://www.nagswithnotions.ie",
    "https://nagswithnotions.ie", 
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

ACCOUNT_EMAIL_VERIFICATION = "none"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email settings
if os.getenv('HEROKU_ENV', 'False') == 'True':
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# Activate Django-Heroku.
django_heroku.settings(locals())

