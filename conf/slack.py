from slacker import Slacker
import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # conf

with open(os.path.join(BASE_DIR, 'secrets.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)

SLACK_TOKEN = secrets['SLACK_TOKEN']

def slack_notify(text=None, channel='#channel_name', username='알림봇', attachments=None):
    slack = Slacker(SLACK_TOKEN)
    slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)
