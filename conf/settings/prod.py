import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = True

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES = {
    'default': secrets['DB_SETTINGS']['PRODUCTION']
}

CORS_ORIGIN_ALLOW_ALL = True  # 일단 TRUE -> 나중에 바꾸기
CORS_ORIGIN_ALLOW_WHITELIST = [
    'https://veeto-cli.gywls517.now.sh',
]

sentry_sdk.init(
    dsn=secrets['SENTRY_ADDRESS'],
    integrations=[DjangoIntegration()]
)
