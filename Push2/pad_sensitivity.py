# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/pad_sensitivity.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from collections import namedtuple
playing_profile = 0
default_profile = 1
loop_selector_profile = 2
MONO_AFTERTOUCH_ENABLED = 1
MONO_AFTERTOUCH_DISABLED = 0
PadSettings = namedtuple('PadSettings', ['sensitivity', 'aftertouch_enabled'])

def index_to_pad_coordinate(index):
    u"""
    Maps a linear range to appropriate x and y coordinates of the pad matrix.
    The coordinates are 1-based, since the pad sensitivity sysex commands expect this
    when setting individual pads.
    """
    x, y = divmod(index, 8)
    return (
     8 - x, y + 1)


def pad_parameter_sender(global_control, pad_control, aftertouch_control):
    u"""
    Sends the pad setting parameters for a given pad, or all pads
    (pad == None) over the given SysexElement.
    """

    def do_send(pad_settings, pad=None):
        if pad is None:
            global_control.send_value(0, 0, pad_settings.sensitivity)
            aftertouch_control.send_value(0, 0, pad_settings.aftertouch_enabled)
        else:
            scene, track = index_to_pad_coordinate(pad)
            pad_control.send_value(scene, track, pad_settings.sensitivity)
            aftertouch_control.send_value(scene, track, pad_settings.aftertouch_enabled)
        return

    return do_send