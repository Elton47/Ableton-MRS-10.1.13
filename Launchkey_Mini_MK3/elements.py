# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini_MK3/elements.py
# Compiled at: 2020-04-14 16:27:38
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import ComboElement
from novation.launchkey_elements import LaunchkeyElements

class Elements(LaunchkeyElements):

    def __init__(self, *a, **k):
        super(Elements, self).__init__(*a, **k)

        def with_shift(button):
            return ComboElement(control=button, modifier=self.shift_button, name=('{}_With_Shift').format(button.name))

        self.play_button_with_shift = with_shift(self.play_button)
        self.record_button_with_shift = with_shift(self.record_button)
        self.scene_launch_button_with_shift = with_shift(self.scene_launch_buttons_raw[0])
        self.stop_solo_mute_button_with_shift = with_shift(self.scene_launch_buttons_raw[1])