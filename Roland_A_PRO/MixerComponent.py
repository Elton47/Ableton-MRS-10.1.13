# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_A_PRO/MixerComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.MixerComponent import MixerComponent as MixerComponentBase
from _Framework.Control import ButtonControl

class MixerComponent(MixerComponentBase):
    bank_up_button = ButtonControl()
    bank_down_button = ButtonControl()
    track_up_button = ButtonControl()
    track_down_button = ButtonControl()

    def __init__(self, *a, **k):
        super(MixerComponent, self).__init__(*a, **k)

    @bank_up_button.pressed
    def bank_up_button_pressed(self, button):
        new_offset = self._track_offset + len(self._channel_strips)
        if len(self.tracks_to_use()) > new_offset:
            self.set_track_offset(new_offset)

    @bank_down_button.pressed
    def bank_down_button_pressed(self, button):
        self.set_track_offset(max(0, self._track_offset - len(self._channel_strips)))

    @track_up_button.pressed
    def track_up_button_pressed(self, button):
        new_offset = self._track_offset + 1
        if len(self.tracks_to_use()) > new_offset:
            self.set_track_offset(new_offset)

    @track_down_button.pressed
    def track_down_button_pressed(self, button):
        self.set_track_offset(max(0, self._track_offset - 1))