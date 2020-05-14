# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/iRig_Keys_IO/session_ring.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens
from ableton.v2.control_surface.components import SessionRingComponent

class SelectedTrackFollowingSessionRingComponent(SessionRingComponent):

    def __init__(self, *a, **k):
        super(SelectedTrackFollowingSessionRingComponent, self).__init__(*a, **k)
        self.__on_selected_track_changed.subject = self.song.view
        self.__on_selected_track_changed()

    @listens('selected_track')
    def __on_selected_track_changed(self):
        tracks_to_use = self.tracks_to_use()
        selected_track = self.song.view.selected_track
        if selected_track in tracks_to_use:
            track_index = list(tracks_to_use).index(selected_track)
            new_offset = track_index - track_index % self.num_tracks
            self.track_offset = new_offset