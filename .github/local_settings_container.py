import os

if os.getenv('OAUTH_CONSUMER_KEY'):
	OAUTH_CONSUMER_KEY = os.getenv('OAUTH_CONSUMER_KEY')
else:
	OAUTH_CONSUMER_KEY = "initial_migration_dummy_value"
if os.getenv('OAUTH_CONSUMER_SECRET'):
	OAUTH_CONSUMER_SECRET = os.getenv('OAUTH_CONSUMER_SECRET')
else:
	OAUTH_CONSUMER_SECRET = "initial_migration_dummy_value"
if os.getenv('SECRET_KEY'):
	SECRET_KEY = os.getenv('SECRET_KEY')
else:
	SECRET_KEY = "initial_migration_dummy_value"
if os.getenv('API_HOST'):
	API_HOST = os.getenv('API_HOST')
if os.getenv('API_PORTAL'):
	API_PORTAL = os.getenv('API_PORTAL')
if os.getenv('CALLBACK_BASE_URL'):
	CALLBACK_BASE_URL = os.getenv('CALLBACK_BASE_URL')
if os.getenv('ALLOWED_HOSTS'):
	ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
if os.getenv('CSRF_TRUSTED_ORIGINS'):
	CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(',')
if os.getenv('CORS_ORIGIN_WHITELIST'):
	CORS_ORIGIN_WHITELIST = os.getenv('CORS_ORIGIN_WHITELIST').split(',')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
