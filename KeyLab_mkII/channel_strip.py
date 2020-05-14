# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/channel_strip.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.control import TextDisplayControl
from KeyLab_Essential.channel_strip import ChannelStripComponent as ChannelStripComponentBase

class ChannelStripComponent(ChannelStripComponentBase):
    track_name_display = TextDisplayControl(' ')

    def set_track_name_display(self, display):
        self.track_name_display.set_control_element(display)
        self._update_track_name_display()

    def set_track(self, track):
        super(ChannelStripComponent, self).set_track(track)
        self._update_track_name_display()

    def _update_track_name_display(self):
        track = self._track
        self.track_name_display[0] = track.name if liveobj_valid(track) else ''