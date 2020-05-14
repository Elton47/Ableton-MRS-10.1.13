# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_A/__init__.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .komplete_kontrol_a import Komplete_Kontrol_A
from ableton.v2.control_surface.capabilities import SUGGESTED_PORT_NAMES_KEY

def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: [
                                'Komplete Kontrol A DAW', 'Komplete Kontrol M DAW']}


def create_instance(c_instance):
    return Komplete_Kontrol_A(c_instance=c_instance)