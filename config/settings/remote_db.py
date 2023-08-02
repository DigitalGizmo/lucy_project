from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Custom setting
ASSET_PATH = "http://lucy-proto.deerfield-ma.org/assets"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lucy_db',
        'USER': 'lucy_db_user',
        'PASSWORD': get_secret("DB_PASS"),
        'HOST': '174.138.62.176', # digital ocean remote
        'PORT': '5432',        
    }
}