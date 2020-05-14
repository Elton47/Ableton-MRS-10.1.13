# MIDI Remote Scripts
# maschine / ableton
#
# maschine_matrix_modes.py
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

import Live  # noqa
from ableton.v2.base.event import listens
from ableton.v2.control_surface.mode import ModesComponent


class MaschineMatrixModes(ModesComponent):

    __events__ = ('is_enabled',)

    def __init__(self, playable=None, selection_matrix=None, *a, **k):
        super(MaschineMatrixModes, self).__init__(*a, **k)
        self._playable = playable
        self._selection_matrix = selection_matrix
        self.add_mode('playable_mode', playable)
        self.add_mode('selection_matrix_mode', selection_matrix)
        self._matrix_enabled = selection_matrix.is_enabled()
        self.__on_is_enabled_changed.subject = selection_matrix

    @property
    def is_enabled(self):
        return self._matrix_enabled

    @listens('selected_mode')
    def __on_selected_mode_changed(self, mode):
        pass
