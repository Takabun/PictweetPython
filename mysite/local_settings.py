import os

#AWS関連
# SECRET_KEY = '1+nrn&gh&=d^f65&+jf!m%k#ilcg11j4(25hnsg11*7zeg(45v'


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True