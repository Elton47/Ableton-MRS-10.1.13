# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK2/consts.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
PRODUCT_ID_BYTE_PREFIX = (0, 32, 41)
LAUNCHKEY_25_ID_BYTE = 123
LAUNCHKEY_49_ID_BYTE = 124
LAUNCHKEY_61_ID_BYTE = 125
PRODUCT_ID_BYTES = (
 LAUNCHKEY_25_ID_BYTE, LAUNCHKEY_49_ID_BYTE, LAUNCHKEY_61_ID_BYTE)
IDENTITY_REQUEST = (240, 126, 127, 6, 1, 247)
IN_CONTROL_QUERY = (159, 11, 0)
DRUM_IN_CONTROL_ON_MESSAGE = (159, 15, 127)
DRUM_IN_CONTROL_OFF_MESSAGE = (159, 15, 0)
STANDARD_CHANNEL = 15
PULSE_LED_CHANNEL = 2
BLINK_LED_CHANNEL = 1
MAX_SENDS = 6