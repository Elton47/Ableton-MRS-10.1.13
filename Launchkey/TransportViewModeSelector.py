# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey/TransportViewModeSelector.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ModeSelectorComponent import ModeSelectorComponent

class TransportViewModeSelector(ModeSelectorComponent):
    """' Class that reassigns specific buttons based on the views visible in Live """
    __module__ = __name__

    def __init__(self, transport, session, ffwd_button, rwd_button):
        ModeSelectorComponent.__init__(self)
        self._transport = transport
        self._session = session
        self._ffwd_button = ffwd_button
        self._rwd_button = rwd_button
        self._app_view().add_is_view_visible_listener('Session', self._on_view_changed)
        self.update()

    def disconnect(self):
        ModeSelectorComponent.disconnect(self)
        self._transport = None
        self._session = None
        self._ffwd_button = None
        self._rwd_button = None
        self._app_view().remove_is_view_visible_listener('Session', self._on_view_changed)
        return

    def update(self):
        super(TransportViewModeSelector, self).update()
        if self.is_enabled():
            if self._mode_index == 0:
                self._transport.set_seek_buttons(self._ffwd_button, self._rwd_button)
                self._session.set_select_buttons(None, None)
            else:
                self._transport.set_seek_buttons(None, None)
                self._session.set_select_buttons(self._ffwd_button, self._rwd_button)
        return

    def _app_view(self):
        return self.application().view

    def _on_view_changed(self):
        if self._app_view().is_view_visible('Session'):
            self._mode_index = 1
        else:
            self._mode_index = 0
        self.update()