# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/APC40_MkII/__init__.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, SYNC, REMOTE, controller_id, inport, outport
from .APC40_MkII import APC40_MkII

def create_instance(c_instance):
    return APC40_MkII(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[41], model_name='Akai APC40 MkII'), 
       PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 outport(props=[SYNC, SCRIPT, REMOTE])]}