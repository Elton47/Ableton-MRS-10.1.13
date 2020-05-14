# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/disconnectable.py
# Compiled at: 2019-10-11 21:52:11
from __future__ import absolute_import, print_function, unicode_literals
from .util import find_if

class Disconnectable(object):
    """'
    Represents an entity that holds connections to other objects that
    should be explicitly cleared to avoid object lifetime problems or
    leaking listeners.
    """
    __module__ = __name__

    def disconnect(self):
        pass


class CompoundDisconnectable(Disconnectable):
    """'
    Compound disconnectable. Collects other disconnectables and
    disconnects them recursively.
    """
    __module__ = __name__

    def __init__(self, *a, **k):
        super(CompoundDisconnectable, self).__init__(*a, **k)
        self._registered_disconnectables = []

    def register_disconnectables(self, disconnectables):
        for disconnectable in disconnectables:
            self.register_disconnectable(disconnectable)

        return disconnectables

    def register_disconnectable(self, slot):
        if slot not in self._registered_disconnectables:
            self._registered_disconnectables.append(slot)
        return slot

    def unregister_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)

    def disconnect_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)
            slot.disconnect()

    def find_disconnectable(self, predicate):
        return find_if(predicate, self._registered_disconnectables)

    def has_disconnectable(self, slot):
        return slot in self._registered_disconnectables

    def disconnect(self):
        for slot in self._registered_disconnectables:
            slot.disconnect()

        self._registered_disconnectables = []
        super(CompoundDisconnectable, self).disconnect()


class disconnectable(object):
    """'
    Context manager that will disconnect the given disconnectable when
    the context is exited.  It returns the original disconnectable.
    """
    __module__ = __name__

    def __init__(self, managed=None, *a, **k):
        super(disconnectable, self).__init__(*a, **k)
        self._managed = managed

    def __enter__(self):
        managed = self._managed
        return managed

    def __exit__(self, *a, **k):
        if self._managed is not None:
            self._managed.disconnect()
        return