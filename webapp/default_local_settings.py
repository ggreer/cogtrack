DEBUG = True
TEMPLATE_DEBUG = DEBUG

COGTRACK_FOLDER="/Users/username/cogtrack/"

# Dev config using sqlite
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = COGTRACK_FOLDER + 'webapp/cogtrack.db'  # devs: change this to whatever path you use.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Absolute path to the directory that holds media.
MEDIA_ROOT = COGTRACK_FOLDER + 'static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    COGTRACK_FOLDER + "templates/"
)

# Set this to false in production
LOCAL_DEVELOPMENT = True

# TODO: Print this only once.
print "COGTRACK_FOLDER is " + COGTRACK_FOLDER
# We want Django 1.1, but most stuff should work on 1.0.4
from django import VERSION as DJANGO_VERSION
print "Django version is %i.%i" % (DJANGO_VERSION[0], DJANGO_VERSION[1])
#assert (1,1) == DJANGO_VERSION[:2], DJANGO_VERSION # Uncomment this line to die if we're not using 1.1
