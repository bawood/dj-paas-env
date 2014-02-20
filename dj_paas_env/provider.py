import os

HEROKU = 'heroku'
OPENSHIFT = 'openshift'
UNKNOWN = 'unknown'


def detect(env=os.environ):
    """
    >>> detect({'DYNO':None})
    'heroku'

    >>> detect({'OPENSHIFT_xxx':None})
    'openshift'

    >>> detect({'xxx':None})
    'unknown'
    """
    if 'DYNO' in env:
        return HEROKU
    for varname in env:
        if varname.startswith('OPENSHIFT_'):
            return OPENSHIFT
    return UNKNOWN
