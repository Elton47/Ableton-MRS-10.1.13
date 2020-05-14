# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/scroll.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import ScrollComponent as ScrollComponentBase
from ableton.v2.control_surface.control import ButtonControl

class ScrollComponent(ScrollComponentBase):
    scroll_up_button = ButtonControl(color='DefaultButton.Off', pressed_color='DefaultButton.On')
    scroll_down_button = ButtonControl(color='DefaultButton.Off', pressed_color='DefaultButton.On')

    @scroll_up_button.pressed
    def scroll_up_button(self, button):
        self.scroll_up()

    @scroll_up_button.released
    def scroll_up_button(self, _):
        self._update_scroll_buttons()

    @scroll_down_button.pressed
    def scroll_down_button(self, button):
        self.scroll_down()

    @scroll_down_button.released
    def scroll_down_button(self, _):
        self._update_scroll_buttons()

    def _update_scroll_buttons(self):
        if not self.scroll_down_button.is_pressed and not self.scroll_up_button.is_pressed:
            self._do_update_scroll_buttons()

    def _do_update_scroll_buttons(self):
        self.scroll_up_button.enabled = self.can_scroll_up()
        self.scroll_down_button.enabled = self.can_scroll_down()