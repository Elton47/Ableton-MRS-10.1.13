# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/ButtonSysexControl.py
# Compiled at: 2019-10-11 21:52:10
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.SysexValueControl import SysexValueControl

class ButtonSysexControl(SysexValueControl):
    """'
    A SysexValueControl that behaves like a button so it can be used as a mode button of
    the ModesComponent.
    """
    __module__ = __name__

    def set_light(self, value):
        pass

    def is_momentary(self):
        return False