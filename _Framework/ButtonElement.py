# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/ButtonElement.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
import Live
from .InputControlElement import InputControlElement, MIDI_CC_TYPE
from .Skin import Skin, SkinColorMissingError
from .Util import nop

class ButtonValue(object):
    """'
    Basic type for button values, so global constants are symbolically
    different from integers.
    """
    __module__ = __name__
    midi_value = 0

    def __init__(self, midi_value=None, *a, **k):
        super(ButtonValue, self).__init__(*a, **k)
        if midi_value is not None:
            self.midi_value = midi_value
        return

    def __int__(self):
        return self.midi_value

    def __eq__(self, other):
        try:
            return id(self) == id(other) or self.midi_value == other
        except NotImplementedError:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return self != OFF_VALUE


ON_VALUE = ButtonValue(127)
OFF_VALUE = ButtonValue(0)

class Color(ButtonValue):
    """'
    Basic interface for showing a color.
    """
    __module__ = __name__

    def draw(self, interface):
        u"""
        Draws the color into the interface.  Depending on the color
        type, interface might be required special capabilities.
        """
        interface.send_value(self.midi_value)


class DummyUndoStepHandler(object):

    def begin_undo_step(self):
        pass

    def end_undo_step(self):
        pass


class ButtonElementMixin(object):
    """'
    Mixin for sending values to button-like control-elements elements.
    """
    __module__ = __name__

    def set_light(self, is_turned_on):
        if is_turned_on:
            self.turn_on()
        else:
            self.turn_off()

    def turn_on(self):
        self.send_value(ON_VALUE)

    def turn_off(self):
        self.send_value(OFF_VALUE)


class ButtonElement(InputControlElement, ButtonElementMixin):
    """'
    Class representing a button a the controller
    """
    __module__ = __name__

    class ProxiedInterface(InputControlElement.ProxiedInterface, ButtonElementMixin):
        is_momentary = nop
        is_pressed = nop

    def __init__(self, is_momentary, msg_type, channel, identifier, skin=Skin(), undo_step_handler=DummyUndoStepHandler(), *a, **k):
        super(ButtonElement, self).__init__(msg_type, channel, identifier, *a, **k)
        self.__is_momentary = bool(is_momentary)
        self._last_received_value = -1
        self._undo_step_handler = undo_step_handler
        self._skin = skin

    def is_momentary(self):
        u""" returns true if the buttons sends a message on being released """
        return self.__is_momentary

    def message_map_mode(self):
        assert self.message_type() is MIDI_CC_TYPE
        return Live.MidiMap.MapMode.absolute

    def is_pressed(self):
        return self.__is_momentary and int(self._last_received_value) > 0

    def set_light(self, value):
        self._set_skin_light(value)

    def _set_skin_light(self, value):
        try:
            color = self._skin[value]
            color.draw(self)
        except SkinColorMissingError:
            super(ButtonElement, self).set_light(value)

    def receive_value(self, value):
        pressed_before = self.is_pressed()
        self._last_received_value = value
        if not pressed_before and self.is_pressed():
            self._undo_step_handler.begin_undo_step()
        super(ButtonElement, self).receive_value(value)
        if pressed_before and not self.is_pressed():
            self._undo_step_handler.end_undo_step()

    def disconnect(self):
        super(ButtonElement, self).disconnect()
        self._undo_step_handler = None
        return