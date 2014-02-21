import os
from urlparse import urlparse

def config(env=os.environ):
    if 'DATABASE_URL' in env:
        return parse(env[''DATABASE_URL''])

ENGINES = {
    'postgres': 'django.db.backends.postgresql_psycopg2',
    'postgresql': 'django.db.backends.postgresql_psycopg2'
}

def parse(url):
    """
    >>> parse('postgresql://ad_mingpxxnxy:ca5Dp1_yFet3@127.11.207.130:5432')
    {'ENGINE': 'django.db.backends.postgresql_psycopg2', 'USERNAME': 'ad_mingpxxnxy', 'NAME': '', 'HOST': '127.11.207.130', 'PASSWORD': 'ca5Dp1_yFet3', 'PORT': 5432}
    >>> parse('postgres://hleulxsesqdumt:vULaPXW9n4eGKK64d2_ujxLqGG@ec2-107-20-214-225.compute-1.amazonaws.com:5432/dcj1n178peejs9')
    {'ENGINE': 'django.db.backends.postgresql_psycopg2', 'USERNAME': 'hleulxsesqdumt', 'NAME': 'dcj1n178peejs9', 'HOST': 'ec2-107-20-214-225.compute-1.amazonaws.com', 'PASSWORD': 'vULaPXW9n4eGKK64d2_ujxLqGG', 'PORT': 5432}
    """
    url = urlparse(url)
    return {
        'ENGINE': ENGINES[url.scheme],
        'NAME': url.path[1:],
        'USERNAME': url.username or '',
        'PASSWORD': url.password or '',
        'HOST': url.hostname,
        'PORT': url.port
    }
