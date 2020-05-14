# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/pad_button_element.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import const
from ableton.v2.control_surface.elements import ButtonElement

class PadButtonElement(ButtonElement):
    """'
    Button element for holding Push pressure-sensitive pad. The pad_id
    parameter defines the Pad coordine id used in the sysex protocol.
    """
    __module__ = __name__

    class ProxiedInterface(ButtonElement.ProxiedInterface):
        sensitivity_profile = const(None)

    def __init__(self, pad_id=None, pad_sensitivity_update=None, *a, **k):
        assert pad_id is not None
        super(PadButtonElement, self).__init__(*a, **k)
        self._sensitivity_profile = 'default'
        self._pad_id = pad_id
        self._pad_sensitivity_update = pad_sensitivity_update
        return

    def _get_sensitivity_profile(self):
        return self._sensitivity_profile

    def _set_sensitivity_profile(self, profile):
        if profile != self._sensitivity_profile and self._pad_sensitivity_update is not None:
            self._sensitivity_profile = profile
            self._pad_sensitivity_update.set_pad(self._pad_id, profile)
        return

    sensitivity_profile = property(_get_sensitivity_profile, _set_sensitivity_profile)

    def reset(self):
        self.sensitivity_profile = 'default'
        super(PadButtonElement, self).reset()