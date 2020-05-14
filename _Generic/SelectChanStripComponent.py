# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/SelectChanStripComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ChannelStripComponent import ChannelStripComponent

class SelectChanStripComponent(ChannelStripComponent):
    """' Subclass of channel strip component that selects tracks that it arms """
    __module__ = __name__

    def __init__(self):
        ChannelStripComponent.__init__(self)

    def _arm_value(self, value):
        assert self._arm_button != None
        assert value in range(128)
        if self.is_enabled():
            track_was_armed = False
            if self._track != None and self._track.can_be_armed:
                track_was_armed = self._track.arm
            ChannelStripComponent._arm_value(self, value)
            if self._track != None and self._track.can_be_armed:
                if self._track.arm and not track_was_armed:
                    if self._track.view.select_instrument():
                        self.song().view.selected_track = self._track
        return