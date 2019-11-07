import os
from .base import *

DEBUG =True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'veeto_db',
        'USER': 'postgres',
        'PASSWORD': 'veeto5',
        'PORT': 5432,
        "HOST": "127.0.0.1",
    }
}


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True