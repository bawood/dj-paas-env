import os
import re

try:
    from urllib.parse import urlparse  # Python 3
except ImportError:
    from urlparse import urlparse  # Python 2


ENGINES = {
    'postgres': 'django.db.backends.postgresql_psycopg2',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def config(env=os.environ):
    fixed_keys = ('DATABASE_URL', 'OPENSHIFT_POSTGRESQL_DB_URL',
                  'OPENSHIFT_MYSQL_DB_URL', 'CLEARDB_DATABASE_URL')
    re_keys = (r'HEROKU_POSTGRESQL_.+_URL', )
    for fixed_key in fixed_keys:
        if fixed_key in env:
            return parse(env[fixed_key])
    for key in env:
        for re_key in re_keys:
            if re.match(re_key, key):
                return parse(env[key])


def parse(url):
    url = urlparse(url)
    return {
        'ENGINE': ENGINES[url.scheme],
        'NAME': url.path[1:].split('?', 2)[0],
        'USERNAME': url.username or '',
        'PASSWORD': url.password or '',
        'HOST': url.hostname,
        'PORT': url.port or ''
    }
