# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ATOM/translating_background.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import BackgroundComponent

class TranslatingBackgroundComponent(BackgroundComponent):

    def __init__(self, translation_channel, *a, **k):
        super(TranslatingBackgroundComponent, self).__init__(*a, **k)
        self._translation_channel = translation_channel

    def _clear_control(self, name, control):
        prior_control = self._control_map.get(name, None)
        if prior_control:
            if prior_control.name == 'Encoders':
                for encoder in prior_control:
                    encoder.use_default_message()

            prior_control.reset()
        super(TranslatingBackgroundComponent, self)._clear_control(name, control)
        if control:
            control.set_channel(self._translation_channel)
            if control.name == 'Pads':
                for button in control:
                    if button:
                        button.set_light('DefaultButton.RgbOff')

        return

    def update(self):
        super(BackgroundComponent, self).update()