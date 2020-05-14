# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/collection/indexed_dict.py
# Compiled at: 2019-10-11 21:52:11
from __future__ import absolute_import, print_function, unicode_literals
from collections import OrderedDict

class IndexedDict(OrderedDict):
    """' Dictionary whose values are accessible by indices """
    __module__ = __name__

    def __init__(self, *args, **kwds):
        self.__keys = []
        super(IndexedDict, self).__init__(*args, **kwds)

    def __setitem__(self, key, value, *args, **kwds):
        super(IndexedDict, self).__setitem__(key, value, *args, **kwds)
        self.__keys.append(key)

    def __delitem__(self, key, *args, **kwds):
        super(IndexedDict, self).__delitem__(key, *args, **kwds)
        self.__keys.remove(key)

    def clear(self):
        super(IndexedDict, self).clear()
        self.__keys = []

    def popitem(self, last=True):
        item = super(IndexedDict, self).popitem(last)
        self.__keys.pop(-1 if last else 0)
        return item

    def keys(self):
        return self.__keys

    def item_by_index(self, ix):
        u""" Returns (key, value) pair for given index """
        key = self.__keys[ix]
        return (
         key, self[key])

    def key_by_index(self, ix):
        u""" Returns key for given index """
        return self.__keys[ix]

    def value_by_index(self, ix):
        u""" Returns value for given index """
        return self[self.__keys[ix]]

    def index_by_key(self, key):
        u""" Returns index of the given key """
        return self.__keys.index(key)