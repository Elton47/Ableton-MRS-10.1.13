# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/LV2_LX2_LC2_LD2/FaderfoxComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *

class FaderfoxComponent:
    """'Baseclass for a subcomponent for Faderfox controllers."""
    __module__ = __name__
    __module__ = __name__
    __filter_funcs__ = [
     'update_display', 'log']

    def __init__(self, parent):
        FaderfoxComponent.realinit(self, parent)

    def realinit(self, parent):
        self.parent = parent
        self.helper = parent.helper
        self.param_map = parent.param_map

    def log(self, string):
        self.parent.log(string)

    def logfmt(self, fmt, *args):
        args2 = []
        for i in range(0, len(args)):
            args2 += [args[i].__str__()]

        str = fmt % tuple(args2)
        return self.log(str)

    def application(self):
        return self.parent.application()

    def song(self):
        return self.parent.song()

    def send_midi(self, midi_event_bytes):
        self.parent.send_midi(midi_event_bytes)

    def request_rebuild_midi_map(self):
        self.parent.request_rebuild_midi_map()

    def disconnect(self):
        pass

    def build_midi_map(self, script_handle, midi_map_handle):
        pass

    def receive_midi_cc(channel, cc_no, cc_value):
        pass

    def receive_midi_note(channel, status, note, velocity):
        pass

    def refresh_state(self):
        pass

    def update_display(self):
        pass