# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/undo_step_handler.py
# Compiled at: 2020-04-14 16:27:38
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid

class UndoStepHandler(object):
    """'
        Class that keeps a set of clients for the current undo step.
        The first client to ask for an undo step will trigger a new step;
        subsequent clients are just added to the stack. The step is only
        ended when all client have asked for it to be ended.
    """
    __module__ = __name__

    def __init__(self, song=None):
        assert liveobj_valid(song)
        self._song = song
        self._clients = set()

    def _begin_step_with_client(self, client):
        if client not in self._clients:
            self._clients.add(client)
            if len(self._clients) == 1:
                self._song.begin_undo_step()

    def _end_step_with_client(self, client):
        if client in self._clients:
            self._clients.remove(client)
            if len(self._clients) == 0:
                self._song.end_undo_step()

    def begin_undo_step(self, client=None):
        if client:
            self._begin_step_with_client(client)
        else:
            self._song.begin_undo_step()

    def end_undo_step(self, client=None):
        if client:
            self._end_step_with_client(client)
        else:
            self._song.end_undo_step()
            if len(self._clients) > 0:
                self._song.begin_undo_step()