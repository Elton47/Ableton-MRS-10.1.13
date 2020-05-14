# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/control/toggle_button.py
# Compiled at: 2020-04-14 16:27:38
from __future__ import absolute_import, print_function, unicode_literals
from .control import Connectable, control_event, control_color
from .button import ButtonControlBase

class ToggleButtonControl(ButtonControlBase):
    """'
    A Control representing a button that can be toggled on and off.

    The class is extending
    :class:`~ableton.v2.control_surface.control.button.ButtonControlBase`
    by adding a :attr:`toggled` event and colors for the two states.

    :meth:`State.connect_property` can be used to connect the Control with a boolean
    property.
    """
    __module__ = __name__
    toggled = control_event('toggled')

    class State(ButtonControlBase.State, Connectable):
        """'
        State-full representation of the Control.
        """
        __module__ = __name__
        untoggled_color = control_color('DefaultButton.Off')
        toggled_color = control_color('DefaultButton.On')
        requires_listenable_connected_property = True

        def __init__(self, untoggled_color=None, toggled_color=None, *a, **k):
            super(ToggleButtonControl.State, self).__init__(*a, **k)
            if untoggled_color is not None:
                self.untoggled_color = untoggled_color
            if toggled_color is not None:
                self.toggled_color = toggled_color
            self._is_toggled = False
            return

        @property
        def is_toggled(self):
            u"""
            Represents the button's toggled state. If a property is connected to the
            Control, it will not be affected by setting is_toggled.
            """
            return self._is_toggled

        @is_toggled.setter
        def is_toggled(self, toggled):
            if self._is_toggled != toggled:
                self._is_toggled = toggled
                self._send_current_color()

        def connect_property(self, *a):
            u"""
            Creates a bidirectional binding between a boolean property and the button's
            toggled state.
            """
            super(ToggleButtonControl.State, self).connect_property(*a)
            self.is_toggled = self.connected_property_value

        def on_connected_property_changed(self, value):
            self.is_toggled = value

        def _send_button_color(self):
            self._control_element.set_light(self.toggled_color if self._is_toggled else self.untoggled_color)

        def _on_pressed(self):
            super(ToggleButtonControl.State, self)._on_pressed()
            self._is_toggled = not self._is_toggled
            self._call_listener('toggled', self._is_toggled)
            self.connected_property_value = self.is_toggled