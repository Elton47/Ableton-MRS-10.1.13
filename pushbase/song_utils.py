# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/song_utils.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import liveobj_valid

def is_return_track(song, track):
    return track in list(song.return_tracks)


def delete_track_or_return_track(song, track):
    tracks = list(song.tracks)
    if track in tracks:
        track_index = tracks.index(track)
        song.delete_track(track_index)
    else:
        track_index = list(song.return_tracks).index(track)
        song.delete_return_track(track_index)


def find_parent_track(live_object):
    u"""
    Returns either the parent track of a live object or None if one is not found.
    """
    track = live_object
    while liveobj_valid(track) and not isinstance(track, Live.Track.Track):
        track = getattr(track, 'canonical_parent', None)

    return track