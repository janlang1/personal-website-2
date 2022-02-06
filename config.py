import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xe2Z\xf2\xe4\x10\xf34<\x069t8Z\xd8w\x1e'