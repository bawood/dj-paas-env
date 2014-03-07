===========
dj-paas-env
===========

.. image:: https://travis-ci.org/pbacterio/dj-paas-env.png?branch=master
   :target: https://travis-ci.org/pbacterio/dj-paas-env

Helper methods to configure Django database and static files in a PAAS environment.


--------
Database
--------

Automatic configuration discovery
=================================

    DATABASES = {
        'default': dj_paas_env.database.config()
    }

This example tries to figure out the configuration database from the following environment variables::
`DATABASE_URL`, `HEROKU_POSTGRESQL_<color>_URL`, `CLEARDB_DATABASE_URL`, `OPENSHIFT_POSTGRESQL_DB_URL`, `OPENSHIFT_MYSQL_DB_URL`
