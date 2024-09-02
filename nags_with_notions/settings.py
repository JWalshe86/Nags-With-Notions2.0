import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import django_heroku

# Load environment variables from .env file
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",   # Development static files
    BASE_DIR / "assets",   # Additional static files directory
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

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
]

SITE_ID = 1
LOGIN_URL = "login"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
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
    # Local settings or development settings
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# Activate Django-Heroku.
django_heroku.settings(locals())

