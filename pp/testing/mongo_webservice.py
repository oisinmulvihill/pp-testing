# -*- coding: utf-8 -*-
"""
Extension on PkgLib pyramid_server fixture to provide explicit config file
and mongo server configuration and api instance.

PythonPro Limited
"""
import ConfigParser

from pkglib.testing import pyramid_server


class MongoConfiguredWebService(pyramid_server.PyramidTestServer):
    """ Parameters
        ----------
        testing_ini:
            path to this service's config file
        rest_api_class:
            class instance for the REST api
        request:
            py.test fixture request
    """
    def __init__(self, **kwargs):
        self.request = kwargs['request']
        super(MongoConfiguredWebService, self).__init__(**kwargs)
        self.api = kwargs['rest_api_class'](self.uri)

    def pre_setup(self):
        super(MongoConfiguredWebService, self).pre_setup()
        parser = ConfigParser.ConfigParser()
        parser.read(self.config)
        mongo_server = self.request.getfuncargvalue('mongo_server')
        parser.set('app:main', 'mongodb.host', mongo_server.hostname)
        parser.set('app:main', 'mongodb.port', mongo_server.port)
        print(
            "User Service using mongodb at {0}:{1}".format(
                mongo_server.hostname,
                mongo_server.port
            )
        )
        with self.config.open('w') as fp:
            parser.write(fp)
