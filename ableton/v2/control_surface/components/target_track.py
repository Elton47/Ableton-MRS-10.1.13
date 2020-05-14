# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/components/target_track.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens, listens_group, liveobj_valid
from ableton.v2.control_surface import Component

class TargetTrackComponent(Component):
    """'
    Component that can be used to notify other components (such as
    PercussionInstrumentFinder) of the track they should control/listen to
    (the target_track). In this base class, the target_track will always be the
    selected track.
    """
    __module__ = __name__
    __events__ = (u'target_track', )

    def __init__(self, *a, **k):
        super(TargetTrackComponent, self).__init__(*a, **k)
        self._target_track = None
        self._armed_track_list = []
        self.__on_selected_track_changed.subject = self.song.view
        self.__on_selected_track_changed()
        return

    @property
    def target_track(self):
        return self._target_track

    @listens('selected_track')
    def __on_selected_track_changed(self):
        if not self._armed_track_list:
            self._set_target_track()

    def _set_target_track(self):
        new_target = self._target_track
        if self._armed_track_list:
            new_target = self._armed_track_list[(-1)]
        else:
            new_target = self.song.view.selected_track
        if self._target_track != new_target:
            self._target_track = new_target
            self.notify_target_track()


class ArmedTargetTrackComponent(TargetTrackComponent):
    """'
    TargetTrackComponent that monitors the armed status of tracks and designates the
    most recently armed track as the target_track. If no tracks are armed, then the
    target_track will be the selected track.
    """
    __module__ = __name__

    def __init__(self, *a, **k):
        super(ArmedTargetTrackComponent, self).__init__(*a, **k)
        self.__on_tracks_changed.subject = self.song
        self.__on_tracks_changed()

    @property
    def tracks(self):
        return filter(lambda t: liveobj_valid(t) and t.can_be_armed and t.has_midi_input, self.song.tracks)

    @listens('visible_tracks')
    def __on_tracks_changed(self):
        tracks = self.tracks
        self.__on_arm_changed.replace_subjects(tracks)
        self.__on_frozen_state_changed.replace_subjects(tracks)
        self._refresh_armed_track_list()

    @listens_group('arm')
    def __on_arm_changed(self, _):
        self._refresh_armed_track_list()

    @listens_group('is_frozen')
    def __on_frozen_state_changed(self, _):
        self._refresh_armed_track_list()

    def _refresh_armed_track_list(self):
        tracks = self.tracks
        for track in self._armed_track_list:
            if not liveobj_valid(track) or not track.arm or track.is_frozen or track not in tracks:
                self._armed_track_list.remove(track)

        for track in tracks:
            if track.arm and not track.is_frozen and track not in self._armed_track_list:
                self._armed_track_list.append(track)

        self._set_target_track()