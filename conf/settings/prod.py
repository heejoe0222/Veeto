from .base import *


DEBUG = False

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES = {
    'default': secrets['DB_SETTINGS']['PRODUCTION']
}

CORS_ORIGIN_ALLOW_ALL = True  # 일단 TRUE -> 나중에 바꾸기
CORS_ORIGIN_ALLOW_WHITELIST = [
    'http://localhost:8000',
    'http://localhost:3000', #나중에 now 링크 쓰기
    'https://veeto-cli.gywls517.now.sh:3000',
]