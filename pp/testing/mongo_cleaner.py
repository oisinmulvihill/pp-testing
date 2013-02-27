"""
Mongo Cleaner
=============

Pytest plugin to clean mongo server databases
"""

import pytest
from pymongo import Connection


@pytest.fixture(scope='function', autouse=True)
def mongo_cleaner(request):
    """ Warning - don't use this in production! :)
    """
    mongo_server = request.getfuncargvalue('mongo_server')
    conn = Connection(mongo_server.hostname, mongo_server.port)
    print
    print "=" * 80
    print "MongoCleaner dropping databases {}".format(conn.database_names())
    print "=" * 80
    print
    [conn.drop_database(i) for i in conn.database_names()]



