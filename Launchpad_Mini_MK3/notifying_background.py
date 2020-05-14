# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Mini_MK3/notifying_background.py
# Compiled at: 2020-04-14 16:27:38
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ableton.v2.control_surface.components import BackgroundComponent

class NotifyingBackgroundComponent(BackgroundComponent):
    __events__ = (u'value', )

    def register_slot(self, control, *a):
        super(BackgroundComponent, self).register_slot(control, partial(self.__on_control_value, control), 'value')

    def __on_control_value(self, control, value):
        self.notify_value(control, value)