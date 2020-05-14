# MIDI Remote Scripts
# maschine / ableton
#
# maschine_main_modes.py
#
# created by Ahmed Emerah - (MaXaR)
# NI user name: Emerah
# NI: Machine MK3, KK S49 MK2, Komplete 12.
# email: ahmed.emerah@icloud.com
#
# developed under macOS 10.15.x and 10.14.6
# python version: python 2.7.17
# live version: 10.1.9
# tools: VS Code (Free)
#
from __future__ import absolute_import, print_function, unicode_literals


class MaschineMainModes(object):

    # todo: move the 3 main modes to this object to observe track and mode changes.

    def __init__(self, *a, **k):
        super(MaschineMainModes, self).__init__(*a, **k)
