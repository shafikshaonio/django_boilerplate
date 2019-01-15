# SECURITY WARNING: don't run with debug turned on in production!
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['192.168.0.1']  # add domain or live server ip

# EMAIL CONFIG
EMAIL_BACKEND = config('PRODUCTION_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = config('PRODUCTION_EMAIL_HOST')
EMAIL_HOST_PASSWORD = config('PRODUCTION_EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('PRODUCTION_EMAIL_HOST_USER')
EMAIL_PORT = config('PRODUCTION_EMAIL_PORT')
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
