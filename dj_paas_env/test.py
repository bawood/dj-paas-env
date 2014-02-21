from doctest import DocTestSuite
from dj_paas_env import provider, database

suite = DocTestSuite(provider)
suite.addTests(DocTestSuite(database))

def load_tests(loader, tests, ignore):
    tests.addTests(suite)
    return tests
