"""
Django settings for upkeep project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'configureme'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kronos',
    'social.apps.django_app.default',
    'profiles',
    'things',
    'cspreports',
    'tasks',
    'piston',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'upkeep.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'upkeep.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTHENTICATION_BACKENDS = (
    #'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',  # Only needed for admin/superuser
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [] # No passwords allowed


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Social Auth configuration
LOGIN_REDIRECT_URL = SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/error'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/stuff/add'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/profile#social'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/profile#social'
SOCIAL_AUTH_INACTIVE_USER_URL = '/login/inactive'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    # 'social.pipeline.mail.mail_validation',
    #'profiles.pipeline.associate_by_email', This is horribly broken by things like USE_UNIQUE_USER_ID and multiple email addresses
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

# Social Auth Backend configuration
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'configureme'  # https://developers.google.com/identity/protocols/OAuth2?csw=1#Registering
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'configureme'
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True

#SOCIAL_AUTH_TWITTER_KEY = 'configureme'  # http://twitter.com/apps/new
#SOCIAL_AUTH_TWITTER_SECRET = 'configureme'

#SOCIAL_AUTH_FACEBOOK_KEY = 'configureme'  # http://developers.facebook.com/setup/
#SOCIAL_AUTH_FACEBOOK_SECRET = 'configureme'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


# CSP Configuration
# https://django-csp.readthedocs.org/en/latest/configuration.html#configuration-chapter
from django.core.urlresolvers import reverse_lazy
CSP_STYLE_SRC = ["'self'", "maxcdn.bootstrapcdn.com"]  # Only for development
CSP_FONT_SRC = ["'self'", "maxcdn.bootstrapcdn.com"]  # Only for development
CSP_REPORT_URI = reverse_lazy('report_csp')
# Note: https://www.tollmanz.com/content-security-policy-report-samples/ for information on the particulars of reports
# Also: https://www.virtuesecurity.com/blog/abusing-csp-violation-reporting/ for security implications
CSP_REPORTS_EMAIL_ADMINS = False  # Don't spam my inbox


# Job Queue (Celery)
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']

WEB_MANIFEST = {
    "name": "Upkeep Your Stuff",
    "short_name": "Upkeep",
    "start_url": "/",
    "icons": []
}

try:
    from .local_settings import *
except ImportError:
    pass