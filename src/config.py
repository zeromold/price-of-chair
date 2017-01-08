import os

_author_ = 'Phil Cogan'

DEBUG = True
ADMINS = frozenset([
    os.environ.get('ADMIN_EMAIL')
])