import os
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'veeto_db',
        'USER': 'postgres',
        'PASSWORD': 'chj8399302',
        'PORT': 5432,
        "HOST": "127.0.0.1",
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'veeto_db_test',
            'USER': 'postgres',
            'PASSWORD': 'chj8399302',
            'PORT': 5432,
        },
    },
}