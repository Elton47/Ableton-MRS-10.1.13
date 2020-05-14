# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/novation/session_navigation.py
# Compiled at: 2019-12-11 08:03:20
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from .util import skin_scroll_buttons

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        super(SessionNavigationComponent, self).__init__(*a, **k)
        skin_scroll_buttons(self._vertical_banking, 'Session.Navigation', 'Session.NavigationPressed')
        skin_scroll_buttons(self._horizontal_banking, 'Session.Navigation', 'Session.NavigationPressed')
        skin_scroll_buttons(self._vertical_paginator, 'Session.Navigation', 'Session.NavigationPressed')
        skin_scroll_buttons(self._horizontal_paginator, 'Session.Navigation', 'Session.NavigationPressed')