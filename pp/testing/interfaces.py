'''
Created on Jun 14, 2013

@author: Edward Easton
'''
import types

from mock import Mock
from zope.interface import classImplements


def create_interface_mock(interface_class):
    """ Dynamically create a Mock sub class that implements the given Zope
        interface class.

    Adapted from http://programmaticallyspeaking.com/
                            mocking-zope-interfaces.html

    Examples
    --------

    >>> from zope import interface
    >>> class IFoo(interface.Interface):
    >>>    def bar():
    >>>       pass
    >>> IFooMock = create_interface_mock(IFoo)
    >>> foo_mock = IFooMock()
    >>> assert IFoo in interface.providedBy(foo_mock)
    >>> foo_mock.bar.return_value = "BANG!"
    >>> assert foo_mock.bar() == "BANG!"
    >>> # this would raise an error, unlike a normal mock
    >>> # foo_mock.baz()
    """

    # the init method, automatically specifying the interface methods
    def init(self, *args, **kwargs):
        Mock.__init__(self, spec=interface_class.names(),
                      *args, **kwargs)

    # we derive the sub class name from the interface name
    name = interface_class.__name__ + "Mock"

    # create the class object and provide the init method
    klass = types.TypeType(name, (Mock,), {"__init__": init})

    # the new class should implement the interface
    classImplements(klass, interface_class)

    return klass
