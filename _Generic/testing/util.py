# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/testing/util.py
# Compiled at: 2019-10-11 21:52:11
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import const, nop
from ableton.v2.testing import count_calls

class MockControlSurface(object):
    instance_identifier = const(0)
    request_rebuild_midi_map = count_calls()
    show_message = nop
    send_midi = nop

    def __init__(self, *a, **k):
        super(MockControlSurface, self).__init__(*a, **k)
        self._song = Live.Song.Song(num_tracks=4, num_returns=2)

    def song(self):
        return self._song