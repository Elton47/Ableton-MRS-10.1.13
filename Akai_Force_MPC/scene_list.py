# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/scene_list.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from itertools import izip_longest
from ableton.v2.base import listens
from ableton.v2.control_surface import Component
from .scene import MPCSceneComponent

class SceneListComponent(Component):

    def __init__(self, session_ring=None, num_scenes=0, *a, **k):
        super(SceneListComponent, self).__init__(*a, **k)
        assert session_ring is not None
        self._session_ring = session_ring
        self.__on_offsets_changed.subject = session_ring
        self._scenes = [ MPCSceneComponent(parent=self, session_ring=session_ring) for _ in xrange(num_scenes)
                       ]
        self.__on_scene_list_changed.subject = self.song
        self._reassign_scenes()
        return

    def set_scene_launch_buttons(self, buttons):
        for scene, button in izip_longest(self._scenes, buttons or []):
            scene.set_launch_button(button)

    def set_scene_color_controls(self, controls):
        for scene, control in izip_longest(self._scenes, controls or []):
            scene.scene_color_control.set_control_element(control)

    @listens('offset')
    def __on_offsets_changed(self, *a):
        if self.is_enabled():
            self._reassign_scenes()

    @listens('scenes')
    def __on_scene_list_changed(self):
        self._reassign_scenes()

    def _reassign_scenes(self):
        scenes = self.song.scenes
        for index, scene in enumerate(self._scenes):
            scene_index = self._session_ring.scene_offset + index
            scene.set_scene(scenes[scene_index] if len(scenes) > scene_index else None)

        return