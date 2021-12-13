from django.test import TestCase

# Create your tests here.
import environ
env = environ.Env()
environ.Env.read_env()

print(env('test'))
