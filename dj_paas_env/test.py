import doctest
from dj_paas_env import provider

suite = doctest.DocTestSuite(provider)

def load_tests(loader, tests, ignore):
    tests.addTests(suite)
    return tests
