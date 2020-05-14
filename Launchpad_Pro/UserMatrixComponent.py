# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/UserMatrixComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

def _disable_control(control):
    for button in control:
        button.set_enabled(False)


class UserMatrixComponent(ControlSurfaceComponent):
    """'
    "Component" that expects ButtonMatrixElements that hold
    ConfigurableButtonElements, to then turn them off. This
    is done so the buttons' messages can be forwarded to Live's Tracks.
    """
    __module__ = __name__

    def __getattr__(self, name):
        if len(name) > 4 and name[:4] == 'set_':
            return _disable_control
        raise AttributeError(name)