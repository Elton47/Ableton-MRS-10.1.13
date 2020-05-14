# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/SkinDefault.py
# Compiled at: 2020-04-23 17:50:15
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Skin import Skin
from .Colors import Rgb

class Colors:

    class Session:
        ClipEmpty = Rgb.BLACK
        ClipStopped = Rgb.GREEN_HALF
        ClipStarted = Rgb.GREEN
        ClipRecording = Rgb.RED
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        NoScene = Rgb.BLACK
        Scene = Rgb.BLUE_HALF
        SceneTriggered = Rgb.BLUE_BLINK
        ScenePlaying = Rgb.BLUE
        StopClip = Rgb.RED
        StopClipTriggered = Rgb.RED_BLINK


def make_default_skin():
    return Skin(Colors)