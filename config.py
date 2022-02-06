import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xe2Z\xf2\xe4\x10\xf34<\x069t8Z\xd8w\x1e'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'johnkang03@gmail.com'
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True