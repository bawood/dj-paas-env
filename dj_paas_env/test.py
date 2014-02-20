import doctest
from dj_paas_env import provider

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(provider))
    return tests