# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/skin.py
# Compiled at: 2019-12-16 13:48:28
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import merge_skins, Skin
from novation.colors import Rgb
from novation.skin import skin as base_skin

class Colors:

    class Device:
        Navigation = Rgb.DARK_BLUE_HALF
        NavigationPressed = Rgb.WHITE

    class Mode:

        class Device:
            On = Rgb.DARK_BLUE
            Off = Rgb.WHITE_HALF

            class Bank:
                Selected = Rgb.DARK_BLUE
                Available = Rgb.WHITE_HALF

        class Sends:
            On = Rgb.VIOLET
            Off = Rgb.WHITE_HALF

            class Bank:
                Available = Rgb.WHITE_HALF

    class Recording:
        Off = Rgb.WHITE_HALF

    class Transport:
        PlayOff = Rgb.WHITE_HALF
        PlayOn = Rgb.GREEN
        ContinueOff = Rgb.AQUA
        ContinueOn = Rgb.RED_HALF
        CaptureOff = Rgb.BLACK
        CaptureOn = Rgb.CREAM
        TapTempo = Rgb.CREAM

    class Quantization:
        Off = Rgb.RED_HALF
        On = Rgb.AQUA


skin = merge_skins(*(base_skin, Skin(Colors)))