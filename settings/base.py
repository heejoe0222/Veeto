import os, json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_DIR = os.path.join(BASE_DIR, 'conf')
with open(os.path.join(SECRET_DIR, 'secrets.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)