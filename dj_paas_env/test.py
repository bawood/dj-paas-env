import unittest
from dj_paas_env import database, provider
import os


class TestDatabaseParse(unittest.TestCase):

    def test_parse_postgres_heroku(self):
        url = 'postgres://hleulxsesqdumt:vULaPXW9n4eGKK64d2_ujxLqGG@' + \
              'ec2-107-20-214-225.compute-1.amazonaws.com:5432/dcj1n178peejs9'
        parsed = database.parse(url)
        parsed_expect = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dcj1n178peejs9',
            'USERNAME': 'hleulxsesqdumt',
            'PASSWORD': 'vULaPXW9n4eGKK64d2_ujxLqGG',
            'HOST': 'ec2-107-20-214-225.compute-1.amazonaws.com',
            'PORT': 5432
        }
        self.assertDictEqual(parsed, parsed_expect)

    def test_parse_postgres_openshift(self):
        url = 'postgresql://ad_mingpxxnxy:ca5Dp1_yFet3@127.11.207.130:5432'
        parsed = database.parse(url)
        parsed_expect = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USERNAME': 'ad_mingpxxnxy',
            'PASSWORD': 'ca5Dp1_yFet3',
            'HOST': '127.11.207.130',
            'PORT': 5432
        }
        self.assertDictEqual(parsed, parsed_expect)

    def test_parse_mysql_heroku(self):
        url = 'mysql://b819c071b951a9:9ca7bbbb@us-cdbr-east-05.cleardb.net/heroku_ec5fddc308fbe9e?reconnect=true'
        parsed = database.parse(url)
        parsed_expect = {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'heroku_ec5fddc308fbe9e',
            'USERNAME': 'b819c071b951a9',
            'PASSWORD': '9ca7bbbb',
            'HOST': 'us-cdbr-east-05.cleardb.net',
            'PORT': ''
        }
        self.assertDictEqual(parsed, parsed_expect)

    def test_parse_mysql_openshift(self):
        url = 'mysql://admingJmQ37x:MDQ22l6xf1P-@127.11.207.130:3306/'
        parsed = database.parse(url)
        self.assertDictEqual(parsed, {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USERNAME': 'admingJmQ37x',
            'PASSWORD': 'MDQ22l6xf1P-',
            'HOST': '127.11.207.130',
            'PORT': 3306
        })


class TestDatabaseConfig(unittest.TestCase):

    def test_config_heroku_promoted(self):
        env = {'DATABASE_URL': 'postgres://asdf:fdsa@qwer:12345/rewq'}
        conf = database.config(env)
        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'rewq',
            'USERNAME': 'asdf',
            'PASSWORD': 'fdsa',
            'HOST': 'qwer',
            'PORT': 12345
        })

    def test_config_heroku_postgres(self):
        env = {'HEROKU_POSTGRESQL_BLACK_URL': 'postgres://asdf:fdsa@qwer:12345/rewq'}
        conf = database.config(env)
        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'rewq',
            'USERNAME': 'asdf',
            'PASSWORD': 'fdsa',
            'HOST': 'qwer',
            'PORT': 12345
        })

    def test_config_heroku_mysql(self):
        env = {'CLEARDB_DATABASE_URL': 'mysql://asdf:fdsa@qwer:12345/rewq'}
        conf = database.config(env)
        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'rewq',
            'USERNAME': 'asdf',
            'PASSWORD': 'fdsa',
            'HOST': 'qwer',
            'PORT': 12345
        })

    def test_config_openshift_postgres(self):
        env = {'OPENSHIFT_POSTGRESQL_DB_URL': 'postgresql://asdf:fdsa@qwer:12345/rewq'}
        conf = database.config(env)
        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'rewq',
            'USERNAME': 'asdf',
            'PASSWORD': 'fdsa',
            'HOST': 'qwer',
            'PORT': 12345
        })

    def test_config_openshift_mysql(self):
        env = {'OPENSHIFT_MYSQL_DB_URL': 'mysql://asdf:fdsa@qwer:12345/rewq'}
        conf = database.config(env)
        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'rewq',
            'USERNAME': 'asdf',
            'PASSWORD': 'fdsa',
            'HOST': 'qwer',
            'PORT': 12345
        })


class TestProviderDetect(unittest.TestCase):

    def test_detect_heroku(self):
        self.assertEqual(provider.detect({'DYNO': None}), provider.HEROKU)

    def test_detect_openshift(self):
        self.assertEqual(provider.detect({'OPENSHIFT_xxx': None}),
                         provider.OPENSHIFT)

    def test_detect_unknown(self):
        self.assertEqual(provider.detect({'xxx': None}), provider.UNKNOWN)

    def test_detect_use_environ(self):
        os.environ['DYNO'] = ''
        self.assertEqual(provider.detect(), provider.HEROKU)


def suite():
    test_suite = unittest.TestSuite()
    tests = unittest.defaultTestLoader.loadTestsFromName(__name__)
    test_suite.addTests(tests)
    return test_suite

if __name__ == '__main__':
    unittest.main()
