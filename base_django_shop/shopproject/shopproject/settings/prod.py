from .base import *
import environ
env = environ.Env()
environ.Env.read_env()

# settings for prod
SECRET_KEY = env('secret_key')

DEBUG = False
ALLOWED_HOSTS = ['*']
