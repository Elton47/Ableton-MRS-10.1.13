# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/proxy.py
# Compiled at: 2020-04-14 16:27:38
from __future__ import absolute_import, print_function, unicode_literals
from .util import BooleanContext

class ProxyBase(object):
    """'
    Provides a general mechanism for building automatic proxy
    objects. The access is determined between the proxied_object, the
    proxied_interface and the proxy itself following the following rules:

    When getting an attribute:

       - If it is the proxy object, return that.
       - Else if it is in the proxied_object and in the proxied_interface,
         return that of the proxied_object.
       - Else if it is in the proxied_interface, return that.
       - Else, throw an attribute error.

    When setting an attribute, since it is more risky, the rules are stricter.

       - If the the attribute is present in the proxy_interface, but not
         in the proxy, set in the proxy_object.
       - Else if the attribute is not present in the proxy_interface, set it
         in the proxy.
       - If the attribute is present in both the proxy_interface and
         the proxy_object, raise an AttributeError complaining about
         ambiguity.
    """
    __module__ = __name__
    _skip_wrapper_lookup = None

    def __init__(self, *a, **k):
        super(ProxyBase, self).__init__(*a, **k)
        self._skip_wrapper_lookup = BooleanContext()

    def proxy_hasattr(self, attr):
        u"""
        Returns whether the proxy, not the proxied, has an attribute.
        """
        with self._skip_wrapper_lookup():
            return hasattr(self, attr)

    def __getattr__(self, name):
        if not self._skip_wrapper_lookup:
            obj = self.proxied_object
            interface = self.proxied_interface
            if obj and hasattr(interface, name):
                return getattr(obj, name)
            return getattr(interface, name)
        raise AttributeError('Does not have attribute %s' % name)

    def __setattr__(self, name, value):
        obj = self.proxied_object
        interface = self.proxied_interface
        if obj and hasattr(interface, name):
            if self.proxy_hasattr(name):
                raise AttributeError('Ambiguous set attribute: %s proxied: %s' % (name, obj))
            setattr(obj, name, value)
        else:
            if hasattr(interface, name):
                raise AttributeError('Ambiguous set attribute: %s proxied: %s' % (name, obj))
            self.__dict__[name] = value

    @property
    def proxied_object(self):
        return

    @property
    def proxied_interface(self):
        obj = self.proxied_object
        return getattr(obj, 'proxied_interface', obj)


class Proxy(ProxyBase):
    proxied_object = None
    _proxied_interface = None

    @property
    def proxied_interface(self):
        return self._proxied_interface or super(Proxy, self).proxied_interface

    def __init__(self, proxied_object=None, proxied_interface=None, *a, **k):
        super(Proxy, self).__init__(*a, **k)
        self.proxied_object = proxied_object
        self._proxied_interface = proxied_interface