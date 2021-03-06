# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/drum_group.py
# Compiled at: 2020-04-23 15:05:01
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from novation.drum_group import DrumGroupComponent as DrumGroupComponentBase
DEFAULT_SCROLL_POSITION = 9

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, *a, **k):
        super(DrumGroupComponent, self).__init__(*a, **k)
        self._position_scroll._ensure_scroll_one_direction = partial(self._possibly_reset_scroll_position, self._position_scroll)
        self._position_scroll._update_scroll_buttons = partial(self._update_scroll_buttons, self._position_scroll)
        self._page_scroll._ensure_scroll_one_direction = partial(self._possibly_reset_scroll_position, self._page_scroll)
        self._page_scroll._update_scroll_buttons = partial(self._update_scroll_buttons, self._page_scroll)

    def _possibly_reset_scroll_position(self, scroll_component):
        if scroll_component.scroll_up_button.is_pressed and scroll_component.scroll_down_button.is_pressed:
            scroll_component._scroll_task_up.kill()
            scroll_component._scroll_task_down.kill()
            self.position = DEFAULT_SCROLL_POSITION

    def _update_scroll_buttons(self, scroll_component):
        self._update_scroll_button(scroll_component.scroll_up_button, scroll_component.can_scroll_up())
        self._update_scroll_button(scroll_component.scroll_down_button, scroll_component.can_scroll_down())

    def _update_scroll_button(self, button, can_scroll):
        button.enabled = True
        button.color = 'DrumGroup.Navigation' if can_scroll else 'DefaultButton.Disabled'
        button.pressed_color = 'DrumGroup.NavigationPressed' if can_scroll else 'DefaultButton.Disabled'