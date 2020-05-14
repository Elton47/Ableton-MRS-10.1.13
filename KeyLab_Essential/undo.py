# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/undo.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ableton.v2.base import task
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl

class UndoComponent(Component):
    undo_button = ButtonControl(color='DefaultButton.Off')

    def __init__(self, *a, **k):
        super(UndoComponent, self).__init__(*a, **k)
        self._light_undo_button_task = self._tasks.add(task.sequence(task.run(partial(self._set_undo_button_light, 'DefaultButton.On')), task.wait(1.0), task.run(partial(self._set_undo_button_light, 'DefaultButton.Off'))))
        self._light_undo_button_task.kill()

    @undo_button.pressed
    def undo_button(self, _):
        if self.song.can_undo:
            self.song.undo()
            if not self._light_undo_button_task.is_running:
                self._light_undo_button_task.restart()

    def _set_undo_button_light(self, value):
        self.undo_button.color = value