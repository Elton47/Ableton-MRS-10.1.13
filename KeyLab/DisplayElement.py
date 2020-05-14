# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab/DisplayElement.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from itertools import chain
from _Framework.PhysicalDisplayElement import PhysicalDisplayElement

class DisplayElement(PhysicalDisplayElement):
    _ascii_translations = {'\x00': 0, 
       ' ': 32, 
       '%': 37, 
       '1': 49, 
       '2': 50, 
       '3': 51, 
       '4': 52, 
       '5': 53, 
       '6': 54, 
       '7': 55, 
       '8': 56, 
       '9': 57, 
       ':': 58, 
       '?': 63, 
       'A': 65, 
       'B': 66, 
       'C': 67, 
       'D': 68, 
       'E': 69, 
       'F': 70, 
       'G': 71, 
       'H': 72, 
       'I': 73, 
       'J': 74, 
       'K': 75, 
       'L': 76, 
       'M': 77, 
       'N': 78, 
       'O': 79, 
       'P': 80, 
       'Q': 81, 
       'R': 82, 
       'S': 83, 
       'T': 84, 
       'U': 85, 
       'V': 86, 
       'W': 87, 
       'X': 88, 
       'Y': 89, 
       'Z': 90, 
       'a': 97, 
       'b': 98, 
       'c': 99, 
       'd': 100, 
       'e': 101, 
       'f': 102, 
       'g': 103, 
       'h': 104, 
       'i': 105, 
       'j': 106, 
       'k': 107, 
       'l': 108, 
       'm': 109, 
       'n': 110, 
       'o': 111, 
       'p': 112, 
       'q': 113, 
       'r': 114, 
       's': 115, 
       't': 116, 
       'u': 117, 
       'v': 118, 
       'w': 119, 
       'x': 120, 
       'y': 121, 
       'z': 122}

    def _build_display_message(self, display):
        message_string = display.display_string
        first_segment = display._logical_segments[0]
        return chain(first_segment.position_identifier(), self._translate_string(message_string))