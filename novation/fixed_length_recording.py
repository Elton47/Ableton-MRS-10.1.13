# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/novation/fixed_length_recording.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
NUM_LENGTHS = 8

def track_can_record(track):
    return track.can_be_armed and (track.arm or track.implicit_arm)


class FixedLengthRecording(object):
    """'
    Handles recording a fixed length clip
    based on a fixed length setting
    """
    __module__ = __name__

    def __init__(self, song=None, fixed_length_setting=None, *a, **k):
        assert song is not None
        assert fixed_length_setting is not None
        super(FixedLengthRecording, self).__init__(*a, **k)
        self._song = song
        self._fixed_length_setting = fixed_length_setting
        return

    def should_start_recording_in_slot(self, clip_slot):
        return track_can_record(clip_slot.canonical_parent) and not clip_slot.is_recording and not clip_slot.has_clip and self._fixed_length_setting.enabled

    def start_recording_in_slot(self, clip_slot):
        if self.should_start_recording_in_slot(clip_slot):
            clip_slot.fire(record_length=self._fixed_length_setting.get_selected_length(self._song))
        else:
            clip_slot.fire()