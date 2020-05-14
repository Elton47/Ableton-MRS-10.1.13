# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/RemoteSL/RemoteSLComponent.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *

class RemoteSLComponent:
    """'Baseclass for a subcomponent of the RemoteSL.
    Just defines some handy shortcuts to the main scripts functions...
    for more details about the methods, see the RemoteSLs doc strings
    """
    __module__ = __name__

    def __init__(self, remote_sl_parent):
        self.__parent = remote_sl_parent
        self.__support_mkII = False

    def application(self):
        return self.__parent.application()

    def song(self):
        return self.__parent.song()

    def send_midi(self, midi_event_bytes):
        self.__parent.send_midi(midi_event_bytes)

    def request_rebuild_midi_map(self):
        self.__parent.request_rebuild_midi_map()

    def disconnect(self):
        pass

    def build_midi_map(self, script_handle, midi_map_handle):
        pass

    def refresh_state(self):
        pass

    def update_display(self):
        pass

    def cc_status_byte(self):
        return CC_STATUS + SL_MIDI_CHANNEL

    def support_mkII(self):
        return self.__support_mkII

    def set_support_mkII(self, support_mkII):
        self.__support_mkII = support_mkII