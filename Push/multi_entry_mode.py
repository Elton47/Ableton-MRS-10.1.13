# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push/multi_entry_mode.py
# Compiled at: 2019-10-11 21:52:10
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.mode import tomode, Mode

class MultiEntryMode(Mode):
    """'
    Mode wrapper that allows registration in multiple modes
    components.  This wrapper can be entered multiple times and the
    enter method will be called only once.  It will be left when the
    number of times leave_mode is called matches the number of calls
    to enter_mode.
    """
    __module__ = __name__

    def __init__(self, mode=None, *a, **k):
        super(MultiEntryMode, self).__init__(*a, **k)
        self._mode = tomode(mode)
        self._entry_count = 0

    def enter_mode(self):
        if self._entry_count == 0:
            self._mode.enter_mode()
        self._entry_count += 1

    def leave_mode(self):
        assert self._entry_count > 0
        if self._entry_count == 1:
            self._mode.leave_mode()
        self._entry_count -= 1

    @property
    def is_entered(self):
        return self._entry_count > 0