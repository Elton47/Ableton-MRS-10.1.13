# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/novation/channel_strip.py
# Compiled at: 2019-12-16 13:48:28
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens, liveobj_valid
from ableton.v2.control_surface.components import ChannelStripComponent as ChannelStripComponentBase
from ableton.v2.control_surface.control import SendValueControl
from .util import get_midi_color_value_for_track

class ChannelStripComponent(ChannelStripComponentBase):
    empty_color = 'Mixer.EmptyTrack'
    track_color_control = SendValueControl()
    static_color_control = SendValueControl()

    def __init__(self, *a, **k):
        super(ChannelStripComponent, self).__init__(*a, **k)
        self._static_color_value = 0
        self._track_color_value = 0

    def set_static_color_value(self, value):
        if value is not None:
            self._static_color_value = value
            self._update_static_color_control()
        return

    def set_track(self, track):
        super(ChannelStripComponent, self).set_track(track)
        self.__on_track_color_changed.subject = track if liveobj_valid(track) else None
        self.__on_track_color_changed()
        self._update_static_color_control()
        return

    @listens('color')
    def __on_track_color_changed(self):
        self._track_color_value = get_midi_color_value_for_track(self._track)
        self._track_color_changed()

    def _track_color_changed(self):
        self.track_color_control.value = self._track_color_value

    def _update_static_color_control(self):
        self.static_color_control.value = self._static_color_value if liveobj_valid(self._track) else 0