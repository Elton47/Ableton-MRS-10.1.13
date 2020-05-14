# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ZERO8/config.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {'STOP': GENERIC_STOP, 
   'PLAY': GENERIC_PLAY, 
   'REC': GENERIC_REC, 
   'LOOP': GENERIC_LOOP, 
   'RWD': GENERIC_RWD, 
   'FFWD': GENERIC_FFWD}
DEVICE_CONTROLS = (
 GENERIC_ENC1,
 GENERIC_ENC2,
 GENERIC_ENC3,
 GENERIC_ENC4,
 GENERIC_ENC5,
 GENERIC_ENC6,
 GENERIC_ENC7,
 GENERIC_ENC8)
VOLUME_CONTROLS = (
 (
  GENERIC_SLI1, 0),
 (
  GENERIC_SLI2, 1),
 (
  GENERIC_SLI3, 2),
 (
  GENERIC_SLI4, 3),
 (
  GENERIC_SLI5, 4),
 (
  GENERIC_SLI6, 5),
 (
  GENERIC_SLI7, 6),
 (
  GENERIC_SLI8, 7))
TRACKARM_CONTROLS = (
 GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {'TOGGLELOCK': GENERIC_BUT9, 
   'BANKDIAL': -1, 
   'NEXTBANK': GENERIC_PAD5, 
   'PREVBANK': GENERIC_PAD1, 
   'BANK1': 80, 
   'BANK2': 81, 
   'BANK3': 82, 
   'BANK4': 83, 
   'BANK5': 84, 
   'BANK6': 85, 
   'BANK7': 86, 
   'BANK8': 87}
CONTROLLER_DESCRIPTION = {'INPUTPORT': 'ZERO8 MIDI IN 2', 
   'OUTPUTPORT': 'ZERO8 MIDI OUT 2', 
   'CHANNEL': 0}
MIXER_OPTIONS = {'NUMSENDS': 2, 
   'SEND1': (
           (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)), 
   'SEND2': (
           (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)), 
   'PANS': (
          (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)), 
   'MASTERVOLUME': -1}