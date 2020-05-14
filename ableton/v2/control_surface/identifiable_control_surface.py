# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/identifiable_control_surface.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
import logging
from ..base import task
from . import midi
from .control_surface import ControlSurface
logger = logging.getLogger(__name__)

class IdentifiableControlSurface(ControlSurface):
    """'
    Control surface that sends an identity request to verify the right device is
    linked to it.
    If the data bytes of the response start with product_id_bytes, the device will
    call on_identified.
    Data bytes start at index 5 and cannot be longer than 12 bytes.
    """
    __module__ = __name__
    identity_request_delay = 0.0
    identity_request = midi.SYSEX_IDENTITY_REQUEST_MESSAGE

    def __init__(self, product_id_bytes=None, *a, **k):
        super(IdentifiableControlSurface, self).__init__(*a, **k)
        assert product_id_bytes is not None
        assert len(product_id_bytes) < 12
        self._product_id_bytes = product_id_bytes
        self._identity_response_pending = False
        self._request_task = self._tasks.add(task.sequence(task.wait(self.identity_request_delay), task.run(self._send_identity_request)))
        self._request_task.kill()
        return

    def on_identified(self, response_bytes):
        self.refresh_state()

    def port_settings_changed(self):
        self._request_task.restart()

    def process_midi_bytes(self, midi_bytes, midi_processor):
        if midi.is_sysex(midi_bytes) and self._is_identity_response(midi_bytes):
            product_id_bytes = self._extract_product_id_bytes(midi_bytes)
            if product_id_bytes == self._product_id_bytes:
                self._request_task.kill()
                if self._identity_response_pending:
                    self.on_identified(midi_bytes)
                    self._identity_response_pending = False
            else:
                logger.error('MIDI device responded with wrong product id (%s != %s).', str(self._product_id_bytes), str(product_id_bytes))
        else:
            super(IdentifiableControlSurface, self).process_midi_bytes(midi_bytes, midi_processor)

    def _is_identity_response(self, midi_bytes):
        return midi_bytes[3:5] == (
         midi.SYSEX_GENERAL_INFO,
         midi.SYSEX_IDENTITY_RESPONSE_ID)

    def _extract_product_id_bytes(self, midi_bytes):
        return midi_bytes[5:5 + len(self._product_id_bytes)]

    def _send_identity_request(self):
        self._identity_response_pending = True
        self._send_midi(self.identity_request)