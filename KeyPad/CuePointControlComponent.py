# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyPad/CuePointControlComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot

class CuePointControlComponent(ControlSurfaceComponent):
    _toggle_cue_button = None
    _prev_cue_button = None
    _next_cue_button = None

    def __init__(self, *a, **k):
        super(CuePointControlComponent, self).__init__(*a, **k)
        self._on_can_jump_to_prev_cue_changed.subject = self.song()
        self._on_can_jump_to_next_cue_changed.subject = self.song()

    def set_toggle_cue_button(self, button):
        self._toggle_cue_button = button
        self._on_toggle_cue.subject = button

    @subject_slot('value')
    def _on_toggle_cue(self, value):
        if value or not self._toggle_cue_button.is_momentary():
            self.song().set_or_delete_cue()

    def set_prev_cue_button(self, button):
        self._prev_cue_button = button
        self._on_jump_to_prev_cue.subject = button
        self._on_can_jump_to_prev_cue_changed()

    @subject_slot('can_jump_to_prev_cue')
    def _on_can_jump_to_prev_cue_changed(self):
        if self._prev_cue_button != None:
            self._prev_cue_button.set_light(self.song().can_jump_to_prev_cue)
        return

    @subject_slot('value')
    def _on_jump_to_prev_cue(self, value):
        if value or not self._prev_cue_button.is_momentary():
            if self.song().can_jump_to_prev_cue:
                self.song().jump_to_prev_cue()

    def set_next_cue_button(self, button):
        self._next_cue_button = button
        self._on_jump_to_next_cue.subject = button
        self._on_can_jump_to_next_cue_changed()

    @subject_slot('can_jump_to_next_cue')
    def _on_can_jump_to_next_cue_changed(self):
        if self._next_cue_button != None:
            self._next_cue_button.set_light(self.song().can_jump_to_next_cue)
        return

    @subject_slot('value')
    def _on_jump_to_next_cue(self, value):
        if value or not self._next_cue_button.is_momentary():
            if self.song().can_jump_to_next_cue:
                self.song().jump_to_next_cue()