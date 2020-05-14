# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/NumericalDisplaySegment.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.LogicalDisplaySegment import LogicalDisplaySegment

class NumericalDisplaySegment(LogicalDisplaySegment):
    """' Special display segment that only displays numerical values """
    __module__ = __name__

    @staticmethod
    def adjust_string(original, length):
        characters_to_retain = {'0': 48, 
           '1': 49, 
           '2': 50, 
           '3': 51, 
           '4': 52, 
           '5': 53, 
           '6': 54, 
           '7': 55, 
           '8': 56, 
           '9': 57}
        resulting_string = ''
        for char in original:
            if char in characters_to_retain:
                resulting_string = resulting_string + char

        if len(resulting_string) > length:
            resulting_string = resulting_string[:length]
        if len(resulting_string) < length:
            resulting_string = resulting_string.rjust(length)
        return resulting_string

    def __init__(self, width, update_callback):
        LogicalDisplaySegment.__init__(self, width, update_callback)

    def display_string(self):
        resulting_string = ' ' * self._width
        if self._data_source != None:
            resulting_string = NumericalDisplaySegment.adjust_string(self._data_source.display_string(), self._width)
        return resulting_string