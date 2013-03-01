"""
Redis Cleaner
=============

Pytest plugin to clean redis server databases
"""

import pytest


@pytest.fixture(scope='function', autouse=True)
def redis_cleaner(request):
    """ Warning - don't use this in production! :)
    """
    redis_server = request.getfuncargvalue('redis_server')
    print
    print "=" * 80
    print "RedisCleaner flushing all keys from {0}:{1}:{2}".format(
      redis_server.hostname, redis_server.port, redis_server.db)
    print "=" * 80
    print
    redis_server.api.flushdb()
