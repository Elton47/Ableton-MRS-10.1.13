# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MackieControl/__init__.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .MackieControl import MackieControl

def create_instance(c_instance):
    return MackieControl(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2675, product_ids=[6], model_name='MCU Pro USB v3.1'), 
       PORTS_KEY: [
                 inport(props=[SCRIPT, REMOTE]),
                 inport(props=[]),
                 inport(props=[]),
                 inport(props=[]),
                 outport(props=[SCRIPT, REMOTE]),
                 outport(props=[]),
                 outport(props=[]),
                 outport(props=[])]}