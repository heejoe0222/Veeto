from .base import *


DEBUG = False

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES = {
    'default': secrets['DB_SETTINGS']['PRODUCTION']
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_ALLOW_WHITELIST = [
    'localhost:8000'
    'localhost:3000' #나중에 now 링크 쓰기
    'https://veeto-cli.gywls517.now.sh:3000'
]