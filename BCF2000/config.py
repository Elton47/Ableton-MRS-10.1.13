# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/BCF2000/config.py
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
 (
  GENERIC_ENC1, 0),
 (
  GENERIC_ENC2, 0),
 (
  GENERIC_ENC3, 0),
 (
  GENERIC_ENC4, 0),
 (
  GENERIC_ENC5, 0),
 (
  GENERIC_ENC6, 0),
 (
  GENERIC_ENC7, 0),
 (
  GENERIC_ENC8, 0))
VOLUME_CONTROLS = (
 (
  GENERIC_SLI1, -1),
 (
  GENERIC_SLI2, -1),
 (
  GENERIC_SLI3, -1),
 (
  GENERIC_SLI4, -1),
 (
  GENERIC_SLI5, -1),
 (
  GENERIC_SLI6, -1),
 (
  GENERIC_SLI7, -1),
 (
  GENERIC_SLI8, -1))
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
   'BANK1': 65, 
   'BANK2': 66, 
   'BANK3': 67, 
   'BANK4': 68, 
   'BANK5': 69, 
   'BANK6': 70, 
   'BANK7': 71, 
   'BANK8': 72}
CONTROLLER_DESCRIPTIONS = {'INPUTPORT': 'BCF2000', 'OUTPUTPORT': 'BCF2000', 'CHANNEL': 0}
MIXER_OPTIONS = {'NUMSENDS': 2, 
   'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1), 
   'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1), 
   'MASTERVOLUME': -1}