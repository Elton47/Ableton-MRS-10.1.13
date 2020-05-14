# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/view_control.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import find_if, listens, liveobj_valid
from ableton.v2.control_surface.control import ButtonControl
from KeyLab_Essential.view_control import ViewControlComponent as ViewControlComponentBase
MAIN_VIEWS = (u'Session', u'Arranger')

class ViewControlComponent(ViewControlComponentBase):
    document_view_toggle_button = ButtonControl()

    def __init__(self, *a, **k):
        super(ViewControlComponent, self).__init__(*a, **k)
        self.__on_focused_document_view_changed.subject = self.application.view
        self.__on_focused_document_view_changed()

    @document_view_toggle_button.pressed
    def document_view_toggle_button(self, _):
        is_session_visible = self.application.view.is_view_visible('Session', main_window_only=True)
        self.show_view('Arranger' if is_session_visible else 'Session')

    @listens('focused_document_view')
    def __on_focused_document_view_changed(self):
        self.document_view_toggle_button.color = ('View.{}').format(self.application.view.focused_document_view)