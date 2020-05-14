# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_A/view_control_component.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import EncoderControl
NavDirection = Live.Application.Application.View.NavDirection

class ViewControlComponent(Component):
    vertical_encoder = EncoderControl()
    horizontal_encoder = EncoderControl()

    @vertical_encoder.value
    def vertical_encoder(self, value, _):
        direction = NavDirection.up if value < 0 else NavDirection.down
        self.application.view.scroll_view(direction, '', False)

    @horizontal_encoder.value
    def horizontal_encoder(self, value, _):
        direction = NavDirection.left if value < 0 else NavDirection.right
        self.application.view.scroll_view(direction, '', False)