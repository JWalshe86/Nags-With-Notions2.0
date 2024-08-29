import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Directories to look for static files during development
STATICFILES_DIRS = [
    BASE_DIR / "static",   # Development static files
    BASE_DIR / "assets",   # Additional static files directory
]

# Directory where static files are collected for production
STATIC_ROOT = BASE_DIR / "staticfiles"

# Use WhiteNoise to serve static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

print("STATICFILES_DIRS:")
for path in STATICFILES_DIRS:
    print(os.path.abspath(path))

print("STATIC_ROOT:")
print(os.path.abspath(STATIC_ROOT))

# Media files (uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# AWS S3 settings (commented out for now)
# if 'USE_AWS' in os.environ:
#     AWS_STORAGE_BUCKET_NAME = 'nags-with-notions2.0'
#     AWS_S3_REGION_NAME = 'eu-north-1'
#     AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

#     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     STATICFILES_LOCATION = 'static'
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     MEDIAFILES_LOCATION = 'media'

#     STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
#     MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# Set to True during development to see changes immediately
DEBUG = True

CRISPY_TEMPLATE_PACK = "bootstrap4"

SECRET_KEY = os.environ.get("SECRET_KEY")

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
    # "whitenoise.runserver_nostatic",  # Disable WhiteNoise's static file serving
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
    "allauth.account.middleware.AccountMiddleware",  # Added for allauth
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
    "default": dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=600, ssl_require=True)
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeanyapp.com",
    "https://*.herokuapp.com",
    "https://nags-with-notions-f8a098968cba.herokuapp.com",
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
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your-email-password'  # Your email password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

