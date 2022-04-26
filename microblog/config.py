import os

class Config(object):
    SECRET_KEY = os.environ.get('SEKRET_KEY') or 'you-will-never-guess'
