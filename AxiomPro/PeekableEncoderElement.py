# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/AxiomPro/PeekableEncoderElement.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import *

class PeekableEncoderElement(EncoderElement):
    """' Encoder that can be connected and disconnected to a specific parameter """
    __module__ = __name__

    def __init__(self, msg_type, channel, identifier, map_mode):
        EncoderElement.__init__(self, msg_type, channel, identifier, map_mode)
        self._peek_mode = False

    def set_peek_mode(self, peek_mode):
        assert isinstance(peek_mode, type(False))
        if self._peek_mode != peek_mode:
            self._peek_mode = peek_mode
            self._request_rebuild()

    def get_peek_mode(self):
        return self._peek_mode

    def install_connections(self, install_translation_callback, install_mapping_callback, install_forwarding_callback):
        current_parameter = self._parameter_to_map_to
        if self._peek_mode:
            self._parameter_to_map_to = None
        InputControlElement.install_connections(self, install_translation_callback, install_mapping_callback, install_forwarding_callback)
        self._parameter_to_map_to = current_parameter
        return