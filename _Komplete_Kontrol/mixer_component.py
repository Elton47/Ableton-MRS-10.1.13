# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/mixer_component.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from itertools import izip_longest
from ableton.v2.control_surface.components import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):

    def set_mute_button(self, button):
        self._selected_strip.set_mute_button(button)

    def set_solo_button(self, button):
        self._selected_strip.set_solo_button(button)

    def set_track_name_displays(self, displays):
        for strip, display in zip(self._channel_strips, displays or []):
            display.set_data_sources((strip.track_name_data_source(),))

    def set_track_volume_displays(self, displays):
        for strip, display in zip(self._channel_strips, displays or []):
            display.set_data_sources((strip.track_volume_data_source,))

    def set_track_panning_displays(self, displays):
        for strip, display in zip(self._channel_strips, displays or []):
            display.set_data_sources((strip.track_panning_data_source,))

    def set_track_type_displays(self, displays):
        for strip, display in izip_longest(self._channel_strips, displays or []):
            strip.track_type_display.set_control_element(display)

    def set_track_selection_displays(self, displays):
        for strip, display in izip_longest(self._channel_strips, displays or []):
            strip.track_selection_display.set_control_element(display)

    def set_track_mute_displays(self, displays):
        for strip, display in izip_longest(self._channel_strips, displays or []):
            strip.track_mute_display.set_control_element(display)

    def set_track_solo_displays(self, displays):
        for strip, display in izip_longest(self._channel_strips, displays or []):
            strip.track_solo_display.set_control_element(display)

    def set_track_muted_via_solo_displays(self, displays):
        for strip, display in izip_longest(self._channel_strips, displays or []):
            strip.track_muted_via_solo_display.set_control_element(display)