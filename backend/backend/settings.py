"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/

"""


from pathlib import Path
from datetime import timedelta
import environ
import os

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '3.230.139.135',
]


# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'channels_postgres',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'user_sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    "rest_framework_simplejwt.token_blacklist",
    'django_extensions',
    'django.contrib.postgres',
    'users',
    'notification.apps.NotificationConfig',
    'posts.apps.PostsConfig',
    'following.apps.FollowingConfig',
    'comments.apps.CommentsConfig',
    'likes.apps.LikesConfig',
    'postviews.apps.PostviewsConfig',
    'tokens.apps.TokensConfig',
    'bugsreport.apps.BugsConfig',
    'phone_field',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'x_forwarded_for.middleware.XForwardedForMiddleware',
    'user_sessions.middleware.SessionMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://localhost:3000',
    'https://127.0.0.1:3000',
]

CORS_ALLOW_CREDENTIALS = True

# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:3000'
# ]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

NOTIFICATIONS_NOTIFICATION_MODEL = 'notification.Notification'
DJANGO_NOTIFICATIONS_CONFIG = { 'USE_JSONFIELD': True}

# GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')
GEOIP_PATH = '/Users/Suyogya/Projects/BasedBook/backend/geoip'
# GEOIP_COUNTRY = 'GeoLite2-Country.mmdb'
# GEOIP_CITY = 'GeoLite2-City.mmdb'
GEOIP_COUNTRY='dbip-country-lite.mmdb'
GEOIP_CITY='dbip-city-lite.mmdb'



ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = "backend.asgi.application"

# CHANNELS_WS_PROTOCOL = "http"  # Use "http" for regular HTTP proxy
# CHANNELS_WS_HOST = "localhost"  # Proxy server host
# CHANNELS_WS_PORT = 8000

DATABASE_ROUTERS = ["backend.routers.CustomRouter"]

DATABASES = {

    # 'default': {

    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',

    #     'NAME': env('DATABASE_NAME'),

    #     'USER': env('DATABASE_USERNAME'),

    #     'PASSWORD': env('DATABASE_PASSWORD'),

    #     'HOST': 'localhost',

    # },

    'default' : {                                   
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'postgres',
        'HOST' : env('SUPABASE_HOST'),
        'PASSWORD': env('SUPABASE_PW'),
        'PORT': 5432,
        'USER': 'postgres',
        'CERT' : 'prod-ca-2021.crt',             # download this from database/settings and put in your main app folder
    },

    'channels_postgres': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USERNAME'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': 'localhost',
	}

}

CHANNEL_LAYERS = {
    # 'default': {
    #     'BACKEND': 'channels_postgres.core.PostgresChannelLayer',
    #     'CONFIG': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': env('DATABASE_NAME'),
    #         'USER': env('DATABASE_USERNAME'),
    #         'PASSWORD': env('DATABASE_PASSWORD'),
    #         'HOST': 'localhost',
    #         'symmetric_encryption_keys': [SECRET_KEY],
    #     },
    # },
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_ENGINE = 'user_sessions.backends.db'
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True


SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True




AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JWT_AUTH = {
    'JWT_AUTH_COOKIE': 'access_token',
}

JWT_AUTH_COOKIE = 'access_token'
JWT_AUTH_COOKIE_SECURE = True
JWT_AUTH_COOKIE_HTTPONLY = True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
      'backend.authenticate.CustomAuthentication',
      'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    # 'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

    'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
    'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
    'AUTH_COOKIE_SECURE': True,    # Whether the auth cookies should be secure (https:// only).
    'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
    'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
    'AUTH_COOKIE_SAMESITE': 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = env('EMAIL_PASS')
EMAIL_VERIFY_URL = env('VERIFY_EMAIL_URL')
RESET_PASSWORD_URL = env('RESET_PASSWORD_URL')
ENCRYPTION_KEY=env('ENCRYPTION_KEY')
