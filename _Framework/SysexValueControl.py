# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/SysexValueControl.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .InputControlElement import InputControlElement, MIDI_SYSEX_TYPE

class SysexValueControl(InputControlElement):
    """'
    Sysex value control receives a sysex message, identified by a
    prefix.  The value can be requested with a value_enquiry MIDI
    message to the controller.
    """
    __module__ = __name__

    def __init__(self, message_prefix=None, value_enquiry=None, default_value=None, *a, **k):
        super(SysexValueControl, self).__init__(msg_type=MIDI_SYSEX_TYPE, sysex_identifier=message_prefix, *a, **k)
        self._value_enquiry = value_enquiry
        self._default_value = default_value

    def send_value(self, value_bytes):
        self.send_midi(self.message_sysex_identifier() + value_bytes + (247, ))

    def enquire_value(self):
        assert self._value_enquiry != None
        self.send_midi(self._value_enquiry)
        return

    def reset(self):
        if self._default_value != None:
            self.send_value(self._default_value)
        return