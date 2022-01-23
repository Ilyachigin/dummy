import sys
import yaml
import pytest


@pytest.fixture(scope='session')
def env():
    config = yaml.safe_load(open(sys.path[1] + '/env.yml'))
    env = config['ENVIRONMENT']
    return env

