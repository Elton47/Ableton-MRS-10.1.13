# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/selected_track_parameter_provider.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import depends, listens, liveobj_valid
from ableton.v2.control_surface import ParameterProvider
from .mixer_utils import is_set_to_split_stereo
SEND_PARAMETER_NAMES = (u'Send A', u'Send B', u'Send C', u'Send D', u'Send E', u'Send F',
                        u'Send G', u'Send H', u'Send I', u'Send J', u'Send K', u'Send L')

def toggle_arm(track_to_arm, song, exclusive=False):
    if track_to_arm.can_be_armed:
        track_to_arm.arm = not track_to_arm.arm
        if exclusive and (track_to_arm.implicit_arm or track_to_arm.arm):
            for track in song.tracks:
                if track.can_be_armed and track != track_to_arm:
                    track.arm = False


class SelectedTrackParameterProvider(ParameterProvider):

    @depends(song=None)
    def __init__(self, song=None, *a, **k):
        super(SelectedTrackParameterProvider, self).__init__(*a, **k)
        self._track = None
        self._on_selected_track.subject = song.view
        self._on_visible_tracks.subject = song
        self._on_selected_track()
        return

    @property
    def parameters(self):
        if self._track:
            mixer = self._track.mixer_device
            params = [mixer.volume]
            if is_set_to_split_stereo(mixer):
                params += [mixer.left_split_stereo, mixer.right_split_stereo]
            else:
                params += [mixer.panning]
            params += list(mixer.sends)
            return [ self._create_parameter_info(p, n) for n, p in zip(self._track_parameter_names(), params)
                   ]
        return []

    def _track_parameter_names(self):
        assert liveobj_valid(self._track)
        names = (u'Volume', )
        names += (u'L Split', u'R Split') if is_set_to_split_stereo(self._track.mixer_device) else (u'Pan', )
        return names + SEND_PARAMETER_NAMES

    def _create_parameter_info(self, parameter, name):
        raise NotImplementedError()

    @listens('visible_tracks')
    def _on_visible_tracks(self):
        self.notify_parameters()

    @listens('selected_track')
    def _on_selected_track(self):
        self._track = self._on_selected_track.subject.selected_track
        self._on_panning_mode_changed.subject = self._track.mixer_device if liveobj_valid(self._track) else None
        self.notify_parameters()
        return

    @listens('panning_mode')
    def _on_panning_mode_changed(self):
        self.notify_parameters()