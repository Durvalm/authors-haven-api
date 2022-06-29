from .base import *
from .base import env
from django.core.management import utils

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY", default=utils.get_random_secret_key())

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1",]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "info@authors-haven.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"