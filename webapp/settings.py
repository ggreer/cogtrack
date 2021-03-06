# Django settings for cogtrack

#DEBUG = True
#TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Production config using mysql
DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'cogtrack_production'
DATABASE_USER = 'cogtrack'
DATABASE_PASSWORD = ''       # Haha, no way am I putting this in a public repo
DATABASE_HOST = ''
DATABASE_PORT = ''
                           
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Pacific' #TODO: in production we should set web servers to UTC

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/www/cogtrack/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/' #TODO: fixme. Right now I'm just running mongoose to serve up cogtrack/static/

LOCAL_DEVELOPMENT = False

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

AUTH_PROFILE_MODULE = 'main.UserProfile'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#7s#dub_pmma#1$#4u0&3*xmb0-n^8s_3#s_9a=@mk94fq2@-d' #TODO: change this in production. right now it's in a public github repo

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'webapp.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/var/www/cogtrack/templates/"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'webapp.cogtest',
    'webapp.main',
    'webapp.test_react_go_no_go',
)

# Copy default_local_settings.py to local_settings.py and edit accordingly
# local_settings.py is in the .gitignore so you don't have to worry about committing silly stuff
try:
  from local_settings import * # Warning, syntax errors in local_settings.py will be squelched
except:
  pass
