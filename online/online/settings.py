import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l8jyt^qbes)16fvzgx=t_kd3=0ch(&^x02x%rp#q71kewuz%%p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



DEFAULT_FROM_EMAIL = "Bekif Online Shopping <bekiyev@gmail.com>"

try:
    from .email_settings import host, user, password
    EMAIL_HOST=host
    EMAIL_HOST_USER = user
    EMAIL_HOST_PASSWORD = password
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
except:
    pass

SITE_URL = "http://bekif.com/bekif_online_shopping/"
if DEBUG:
    SITE_URL = "http://127.0.0.1:8000"
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'carts',
    'marketing',
    'orders',
    'products',    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketing',
)

ROOT_URLCONF = 'online.urls'

WSGI_APPLICATION = 'online.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MARKETING_HOURS_OFFSET = 2

MARKETING_SECONDS_OFFSET = 0

DEFAULT_TAX_RATE = 0.08

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
#MEDIA_ROOT = '/Users/jmitch/Desktop/online/static/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


STRIPE_SECRET_KEY = "sk_test_DjpyHJ0pwqesZHQhEmbSxIc4"
STRIPE_PUBLISHABLE_KEY = "pk_test_QAeq7frcW2hAM8IV8vz2c3cy"




