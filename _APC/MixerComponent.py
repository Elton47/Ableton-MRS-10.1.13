# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_APC/MixerComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ChannelStripComponent import ChannelStripComponent as ChannelStripComponentBase
from _Framework.MixerComponent import MixerComponent as MixerComponentBase
TRACK_FOLD_DELAY = 5

class ChanStripComponent(ChannelStripComponentBase):
    """' Subclass of channel strip component using select button for (un)folding tracks """
    __module__ = __name__

    def __init__(self, *a, **k):
        super(ChanStripComponent, self).__init__(*a, **k)
        self._toggle_fold_ticks_delay = -1
        self._register_timer_callback(self._on_timer)

    def disconnect(self):
        self._unregister_timer_callback(self._on_timer)
        super(ChanStripComponent, self).disconnect()

    def _select_value(self, value):
        super(ChanStripComponent, self)._select_value(value)
        if self.is_enabled() and self._track != None:
            if self._track.is_foldable and self._select_button.is_momentary() and value != 0:
                self._toggle_fold_ticks_delay = TRACK_FOLD_DELAY
            else:
                self._toggle_fold_ticks_delay = -1
        return

    def _on_timer(self):
        if self.is_enabled() and self._track != None and self._toggle_fold_ticks_delay > -1:
            if not self._track.is_foldable:
                raise AssertionError
                if self._toggle_fold_ticks_delay == 0:
                    self._track.fold_state = not self._track.fold_state
                self._toggle_fold_ticks_delay -= 1
        return


class MixerComponent(MixerComponentBase):
    """' Special mixer class that uses return tracks alongside midi and audio tracks """
    __module__ = __name__

    def tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)

    def _create_strip(self):
        return ChanStripComponent()