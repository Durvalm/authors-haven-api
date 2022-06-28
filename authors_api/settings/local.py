from .base import *
from .base import env
from django.core.management import utils

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY", default=utils.get_random_secret_key())

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1",]
