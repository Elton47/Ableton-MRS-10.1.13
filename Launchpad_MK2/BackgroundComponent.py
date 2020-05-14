# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_MK2/BackgroundComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        if control:
            control.add_value_listener(self._on_value_listener)
        super(BackgroundComponent, self)._clear_control(name, control)

    def _on_value_listener(self, *a, **k):
        pass


class TranslatingBackgroundComponent(BackgroundComponent):

    def __init__(self, translation_channel=0, *a, **k):
        super(TranslatingBackgroundComponent, self).__init__(*a, **k)
        self._translation_channel = translation_channel

    def _clear_control(self, name, control):
        if control:
            control.set_channel(self._translation_channel)
        super(TranslatingBackgroundComponent, self)._clear_control(name, control)