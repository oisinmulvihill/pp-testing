'''
PyTest fixture to set up logging and return a handler

@author: Oisin Mulvihill
'''
import logging

import pytest


@pytest.fixture(scope='session')
def log(request):
    """Log to console.
    """
    l = logging.getLogger()
    hdlr = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s'
    )
    hdlr.setFormatter(formatter)
    l.addHandler(hdlr)
    l.setLevel(logging.DEBUG)
    l.propagate = False

    return l
