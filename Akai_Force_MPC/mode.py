# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/mode.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.mode import Mode

class ExtendComboElementMode(Mode):

    def __init__(self, combo_pairs=None, *a, **k):
        super(ExtendComboElementMode, self).__init__(*a, **k)
        self._combo_pairs = combo_pairs

    def enter_mode(self):
        for combo, nested in self._combo_pairs:
            combo.register_control_element(nested)

    def leave_mode(self):
        for combo, nested in self._combo_pairs:
            combo.unregister_control_element(nested)