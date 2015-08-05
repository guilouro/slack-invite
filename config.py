# coding: utf-8
from os import environ

SLACK_GROUP = environ.get('SLACK_GROUP', 'YOUR_GROUP_NAME')
SLACK_TOKEN = environ.get('SLACK_TOKEN', 'TOKEN_GROUP')
SLACK_URL = 'https://%s.slack.com' % SLACK_GROUP

META_TITLE = environ.get('META_TITLE','METATAG_TITLE')
META_DESCRIPTION = environ.get('META_DESCRIPTION',  'METATAG_DESCRIPTION')

BG_FILENAME = environ.get('BG_FILENAME')
