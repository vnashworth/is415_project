"""
Django settings for is415_project project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import shutil
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

AZURE_API_URL = os.environ.get('AZURE_API_URL')
AZURE_API_KEY = os.environ.get('AZURE_API_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'homepage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'is415_project.urls'

TEMPLATES = [
    {
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'OPTIONS': {
            # functions to automatically add variables to the params/context before templates are rendered
            'CONTEXT_PROCESSORS': [
                'django.template.context_processors.static',            # adds "STATIC_URL" from settings.py
                'django.template.context_processors.debug',             # adds debug and sql_queries
                'django.template.context_processors.request',           # adds "request" object
                'django.contrib.auth.context_processors.auth',          # adds "user" and "perms" objects
                'django.contrib.messages.context_processors.messages',  # adds messages from the messages framework
                'django_mako_plus.context_processors.settings',         # adds "settings" dictionary
            ],

            # identifies where the Mako template cache will be stored, relative to each template directory
            'TEMPLATES_CACHE_DIR': '.cached_templates',

            # the default app and page to render in Mako when the url is too short
            'DEFAULT_PAGE': 'index',
            'DEFAULT_APP': 'homepage',

            # the default encoding of template files
            'DEFAULT_TEMPLATE_ENCODING': 'utf-8',

            # imports for every template
            'DEFAULT_TEMPLATE_IMPORTS': [
                # import DMP (required)
                'import django_mako_plus',

                # uncomment this next line to enable alternative syntax blocks within your Mako templates
                # 'from django_mako_plus import django_syntax, jinja2_syntax, alternate_syntax

                # the next two lines are just examples of including common imports in templates
                # 'from datetime import datetime',
                # 'import os, os.path, re, json',
            ],

            # whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
            # determines whether DMP will send its custom signals during the process
            'SIGNALS': False,

            # # static file providers - these autoinclude *.css and *.js files
            # 'CONTENT_PROVIDERS': [
            #     # generates links for app/styles/template.css
            #     { 'provider': 'django_mako_plus.CssLinkProvider' },
            #
            #     # generates links for app/scripts/template.js
            #     { 'provider': 'django_mako_plus.JsLinkProvider' },
            #
            #     # adds JS context
            #     { 'provider': 'django_mako_plus.JsContextProvider' },
            #
            #     # compiles app/styles/template.scss to app/styles/template/css
            #     { 'provider': 'django_mako_plus.CompileScssProvider' },
            #
            #     # compiles app/styles/template.less to app/styles/template/css
            #     { 'provider': 'django_mako_plus.CompileLessProvider' },
            # ],

            # see the DMP online tutorial for information about this setting
            # it can normally be empty
            'TEMPLATES_DIRS': [
                # '/var/somewhere/templates/',
            ],
        },
    },
    {
        'NAME': 'django',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'is415_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
}
DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=0)



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    #BASE_DIR,
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

WHITENOISE_MAX_AGE = 604800
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# A logger for DMP
DEBUG_PROPAGATE_EXCEPTIONS = False  # SECURITY WARNING: never set this True on a live site
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'dmp_simple': {
            'format': '%(levelname)s::DMP %(message)s'
        },
    },
    'handlers': {
        'dmp_console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'dmp_simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['dmp_console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
