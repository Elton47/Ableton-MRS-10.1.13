# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/device_decorator_factory.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DeviceDecoratorFactory as DeviceDecoratorFactoryBase
from .auto_filter import AutoFilterDeviceDecorator
from .compressor import CompressorDeviceDecorator
from .device_decoration import SamplerDeviceDecorator, PedalDeviceDecorator, DrumBussDeviceDecorator, UtilityDeviceDecorator
from .delay import DelayDeviceDecorator
from .echo import EchoDeviceDecorator
from .eq8 import Eq8DeviceDecorator
from .operator import OperatorDeviceDecorator
from .simpler import SimplerDeviceDecorator
from .wavetable import WavetableDeviceDecorator

class DeviceDecoratorFactory(DeviceDecoratorFactoryBase):
    DECORATOR_CLASSES = {'OriginalSimpler': SimplerDeviceDecorator, 
       'Operator': OperatorDeviceDecorator, 
       'MultiSampler': SamplerDeviceDecorator, 
       'AutoFilter': AutoFilterDeviceDecorator, 
       'Eq8': Eq8DeviceDecorator, 
       'Compressor2': CompressorDeviceDecorator, 
       'Pedal': PedalDeviceDecorator, 
       'DrumBuss': DrumBussDeviceDecorator, 
       'Echo': EchoDeviceDecorator, 
       'InstrumentVector': WavetableDeviceDecorator, 
       'StereoGain': UtilityDeviceDecorator, 
       'Delay': DelayDeviceDecorator}