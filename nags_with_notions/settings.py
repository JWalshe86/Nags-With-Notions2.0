import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

# This is used if you are serving static files from a specific directory in development
STATICFILES_DIRS = [
    BASE_DIR / "assets",  # Adjust the path to where your assets are located
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'nags-with-notions2.0'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static & media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

CRISPY_TEMPLATE_PACK = "bootstrap4"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'www.nagswithnotions.ie',
    'nagswithnotions.ie',
    'nags-with-notions-f8a098968cba.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    "pizza_system.apps.PizzaSystemConfig",
    "booking.apps.BookingConfig",
    "nags_with_notions",
    "whitenoise.runserver_nostatic",
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
]

SITE_ID = 1
LOGIN_URL = "login"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "nags_with_notions.urls"

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

WSGI_APPLICATION = "nags_with_notions.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=600, ssl_require=True)
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeanyapp.com",
    "https://*.herokuapp.com",
    "https://nags-with-notions-f8a098968cba.herokuapp.com",
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

ACCOUNT_EMAIL_VERIFICATION = "none"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

