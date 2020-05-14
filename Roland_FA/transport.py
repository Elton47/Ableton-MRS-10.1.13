# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/transport.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import ButtonControl
from ableton.v2.control_surface.components import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):
    jump_to_start_button = ButtonControl()

    @jump_to_start_button.pressed
    def jump_to_start_button(self, _):
        self.song.current_song_time = 0.0