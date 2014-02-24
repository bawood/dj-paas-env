# coding=utf-8
from setuptools import setup
from sys import version_info

if version_info < (2, 7):
    test_require = ['unittest2']
else:
    test_require = []

setup(
    name='dj-paas-env',
    version='',
    packages=['dj_paas_env'],
    url='',
    license='',
    author='Germán Moya',
    author_email='',
    test_suite='dj_paas_env.test.suite',
    test_require=test_require
)
