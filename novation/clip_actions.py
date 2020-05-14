# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/novation/clip_actions.py
# Compiled at: 2020-04-23 15:05:01
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import duplicate_clip_loop
from ableton.v2.control_surface.components import ClipActionsComponent as ClipActionsComponentBase
from .blinking_button import BlinkingButtonControl

class ClipActionsComponent(ClipActionsComponentBase):
    quantization_component = None
    quantize_button = BlinkingButtonControl(color='Action.Quantize', blink_on_color='Action.QuantizePressed', blink_off_color='Action.Quantize')
    double_loop_button = BlinkingButtonControl(color='Action.Double', blink_on_color='Action.DoublePressed', blink_off_color='Action.Double')

    def __init__(self, *a, **k):
        super(ClipActionsComponent, self).__init__(*a, **k)
        self.delete_button.color = 'Action.Delete'
        self.delete_button.pressed_color = 'Action.DeletePressed'
        self.duplicate_button.color = 'Action.Duplicate'
        self.duplicate_button.pressed_color = 'Action.DuplicatePressed'

    @quantize_button.pressed
    def quantize_button(self, _):
        if self.quantization_component:
            self.quantization_component.quantize_clip(self.clip_slot.clip)
            self.quantize_button.start_blinking()

    @double_loop_button.pressed
    def double_loop_button(self, _):
        duplicate_clip_loop(self.clip_slot.clip)
        self.double_loop_button.start_blinking()

    def _update_action_buttons(self):
        super(ClipActionsComponent, self)._update_action_buttons()
        self.quantize_button.enabled = self._can_perform_clip_action()