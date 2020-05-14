# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/optional.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
from ...base import listens
from .combo import ToggleElement

class ChoosingElement(ToggleElement):
    """'
    An Element wrapper that enables one of the nested elements based on
    the value of the given flag.
    """
    __module__ = __name__

    def __init__(self, flag=None, *a, **k):
        super(ChoosingElement, self).__init__(*a, **k)
        self.__on_flag_changed.subject = flag
        self.__on_flag_changed(flag.value)

    @listens('value')
    def __on_flag_changed(self, value):
        self.set_toggled(value)


class OptionalElement(ChoosingElement):
    """'
    An Element wrapper that enables the nested element IFF some given
    flag is set to a specific value.
    """
    __module__ = __name__

    def __init__(self, control=None, flag=None, value=None, *a, **k):
        on_control = control if value else None
        off_control = None if value else control
        super(OptionalElement, self).__init__(on_control=on_control, off_control=off_control, flag=flag, *a, **k)
        return