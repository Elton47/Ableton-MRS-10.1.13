# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push/global_pad_parameters.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Component
from . import sysex

class GlobalPadParameters(Component):

    def __init__(self, aftertouch_threshold=0, *a, **k):
        super(GlobalPadParameters, self).__init__(*a, **k)
        self._pad_parameter_element = None
        self._aftertouch_threshold = aftertouch_threshold
        return

    def _get_aftertouch_threshold(self):
        return self._aftertouch_threshold

    def _set_aftertouch_threshold(self, value):
        self._aftertouch_threshold = value
        self._update_pad_parameter_element()

    aftertouch_threshold = property(_get_aftertouch_threshold, _set_aftertouch_threshold)

    def set_pad_parameter(self, element):
        self._pad_parameter_element = element
        self._update_pad_parameter_element()

    def _update_pad_parameter_element(self):
        if self._pad_parameter_element:
            self._pad_parameter_element.send_value(sysex.make_pad_parameter_message(aftertouch_threshold=self._aftertouch_threshold))

    def update(self):
        super(GlobalPadParameters, self).update()
        if self.is_enabled():
            self._update_pad_parameter_element()