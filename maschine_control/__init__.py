# MIDI Remote Scripts
# maschine / ableton
#
# __init__.py
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

from .maschine_control_surface import MaschineControlSurface


def create_instance(c_instance):
    return MaschineControlSurface(c_instance)
