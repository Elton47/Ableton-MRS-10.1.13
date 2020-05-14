# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Alesis_VI/Alesis_VI.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurface import ControlSurface
from _Framework.MidiMap import make_encoder, MidiMap as MidiMapBase
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.ButtonElement import ButtonElement
from _Framework.Layer import Layer
from _Framework.TransportComponent import TransportComponent
from _Framework.MixerComponent import MixerComponent

class MidiMap(MidiMapBase):

    def __init__(self, *a, **k):
        super(MidiMap, self).__init__(*a, **k)
        self.add_momentary_button('Stop', 0, 118, MIDI_CC_TYPE)
        self.add_momentary_button('Play', 0, 119, MIDI_CC_TYPE)
        self.add_momentary_button('Loop', 0, 115, MIDI_CC_TYPE)
        self.add_momentary_button('Record', 0, 114, MIDI_CC_TYPE)
        self.add_momentary_button('Forward', 0, 117, MIDI_CC_TYPE)
        self.add_momentary_button('Backward', 0, 116, MIDI_CC_TYPE)
        self.add_matrix('Volume_Encoders', make_encoder, 0, [
         range(20, 32) + [35, 41, 46, 47]], MIDI_CC_TYPE)

    def add_momentary_button(self, name, channel, number, midi_message_type):
        assert name not in self.keys()
        self[name] = ButtonElement(True, midi_message_type, channel, number, name=name)


class Alesis_VI(ControlSurface):

    def __init__(self, *a, **k):
        super(Alesis_VI, self).__init__(*a, **k)
        with self.component_guard():
            midimap = MidiMap()
            transport = TransportComponent(name='Transport', is_enabled=False, layer=Layer(play_button=midimap['Play'], stop_button=midimap['Stop'], loop_button=midimap['Loop'], record_button=midimap['Record'], seek_forward_button=midimap['Forward'], seek_backward_button=midimap['Backward']))
            mixer_size = len(midimap['Volume_Encoders'])
            mixer = MixerComponent(mixer_size, name='Mixer', is_enabled=False, layer=Layer(volume_controls=midimap['Volume_Encoders']))
            transport.set_enabled(True)
            mixer.set_enabled(True)