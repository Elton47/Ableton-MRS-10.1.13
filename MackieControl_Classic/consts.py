# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MackieControl_Classic/consts.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
NOTE_OFF_STATUS = 128
NOTE_ON_STATUS = 144
CC_STATUS = 176
PB_STATUS = 224
SYSEX_DEVICE_TYPE = 20
SYSEX_DEVICE_TYPE_XT = 21
NUM_CHANNEL_STRIPS = 8
MASTER_CHANNEL_STRIP_INDEX = 8
BUTTON_STATE_OFF = 0
BUTTON_STATE_ON = 127
BUTTON_STATE_BLINKING = 1
BUTTON_PRESSED = 1
BUTTON_RELEASED = 0
NUM_CHARS_PER_DISPLAY_LINE = 54
SELECT_SMPTE_NOTE = 113
SELECT_BEATS_NOTE = 114
SELECT_RUDE_SOLO = 115
FID_PANNING_BASE = 16
JOG_WHEEL_CC_NO = 60
VPOT_DISPLAY_SINGLE_DOT = 0
VPOT_DISPLAY_BOOST_CUT = 1
VPOT_DISPLAY_WRAP = 2
VPOT_DISPLAY_SPREAD = 3
CSM_VOLPAN = 0
CSM_PLUGINS = 1
CSM_IO = 2
CSM_SENDS = 3
CSM_IO_MODE_INPUT_MAIN = 0
CSM_IO_MODE_INPUT_SUB = 1
CSM_IO_MODE_OUTPUT_MAIN = 2
CSM_IO_MODE_OUTPUT_SUB = 3
CSM_IO_FIRST_MODE = CSM_IO_MODE_INPUT_MAIN
CSM_IO_LAST_MODE = CSM_IO_MODE_OUTPUT_SUB
PCM_DEVICES = 0
PCM_PARAMETERS = 1
PCM_NUMMODES = 2
CLIP_STATE_INVALID = -1
CLIP_STOPPED = 0
CLIP_TRIGGERED = 1
CLIP_PLAYING = 2
g7_seg_led_conv_table = {' ': 0, 
   'A': 1, 
   'B': 2, 
   'C': 3, 
   'D': 4, 
   'E': 5, 
   'F': 6, 
   'G': 7, 
   'H': 8, 
   'I': 9, 
   'J': 10, 
   'K': 11, 
   'L': 12, 
   'M': 13, 
   'N': 14, 
   'O': 15, 
   'P': 16, 
   'Q': 17, 
   'R': 18, 
   'S': 19, 
   'T': 20, 
   'U': 21, 
   'V': 22, 
   'W': 23, 
   'X': 24, 
   'Y': 25, 
   'Z': 26, 
   '\\': 34, 
   '#': 35, 
   '$': 36, 
   '%': 37, 
   '&': 38, 
   "'": 39, 
   '(': 40, 
   ')': 41, 
   '*': 42, 
   '+': 43, 
   ',': 44, 
   '0': 48, 
   '1': 49, 
   '2': 50, 
   '3': 51, 
   '4': 52, 
   '5': 53, 
   '6': 54, 
   '7': 55, 
   '8': 56, 
   '9': 57, 
   ';': 59, 
   '<': 60}
SID_FIRST = 0
SID_RECORD_ARM_BASE = 0
SID_RECORD_ARM_CH1 = 0
SID_RECORD_ARM_CH2 = 1
SID_RECORD_ARM_CH3 = 2
SID_RECORD_ARM_CH4 = 3
SID_RECORD_ARM_CH5 = 4
SID_RECORD_ARM_CH6 = 5
SID_RECORD_ARM_CH7 = 6
SID_RECORD_ARM_CH8 = 7
SID_SOLO_BASE = 8
SID_SOLO_CH1 = 8
SID_SOLO_CH2 = 9
SID_SOLO_CH3 = 10
SID_SOLO_CH4 = 11
SID_SOLO_CH5 = 12
SID_SOLO_CH6 = 13
SID_SOLO_CH7 = 14
SID_SOLO_CH8 = 15
SID_MUTE_BASE = 16
SID_MUTE_CH1 = 16
SID_MUTE_CH2 = 17
SID_MUTE_CH3 = 18
SID_MUTE_CH4 = 19
SID_MUTE_CH5 = 20
SID_MUTE_CH6 = 21
SID_MUTE_CH7 = 22
SID_MUTE_CH8 = 23
SID_SELECT_BASE = 24
SID_SELECT_CH1 = 24
SID_SELECT_CH2 = 25
SID_SELECT_CH3 = 26
SID_SELECT_CH4 = 27
SID_SELECT_CH5 = 28
SID_SELECT_CH6 = 29
SID_SELECT_CH7 = 30
SID_SELECT_CH8 = 31
SID_VPOD_PUSH_BASE = 32
SID_VPOD_PUSH_CH1 = 32
SID_VPOD_PUSH_CH2 = 33
SID_VPOD_PUSH_CH3 = 34
SID_VPOD_PUSH_CH4 = 35
SID_VPOD_PUSH_CH5 = 36
SID_VPOD_PUSH_CH6 = 37
SID_VPOD_PUSH_CH7 = 38
SID_VPOD_PUSH_CH8 = 39
channel_strip_switch_ids = range(SID_RECORD_ARM_BASE, SID_VPOD_PUSH_CH8 + 1)
SID_ASSIGNMENT_IO = 40
SID_ASSIGNMENT_SENDS = 41
SID_ASSIGNMENT_PAN = 42
SID_ASSIGNMENT_PLUG_INS = 43
SID_ASSIGNMENT_EQ = 44
SID_ASSIGNMENT_DYNAMIC = 45
channel_strip_assignment_switch_ids = range(SID_ASSIGNMENT_IO, SID_ASSIGNMENT_DYNAMIC + 1)
SID_FADERBANK_PREV_BANK = 46
SID_FADERBANK_NEXT_BANK = 47
SID_FADERBANK_PREV_CH = 48
SID_FADERBANK_NEXT_CH = 49
SID_FADERBANK_FLIP = 50
SID_FADERBANK_EDIT = 51
channel_strip_control_switch_ids = range(SID_ASSIGNMENT_IO, SID_FADERBANK_EDIT + 1)
SID_DISPLAY_NAME_VALUE = 52
SID_DISPLAY_SMPTE_BEATS = 53
display_switch_ids = range(SID_DISPLAY_NAME_VALUE, SID_DISPLAY_SMPTE_BEATS + 1)
SID_SOFTWARE_F1 = 54
SID_SOFTWARE_F2 = 55
SID_SOFTWARE_F3 = 56
SID_SOFTWARE_F4 = 57
SID_SOFTWARE_F5 = 58
SID_SOFTWARE_F6 = 59
SID_SOFTWARE_F7 = 60
SID_SOFTWARE_F8 = 61
SID_SOFTWARE_F9 = 62
SID_SOFTWARE_F10 = 63
SID_SOFTWARE_F11 = 64
SID_SOFTWARE_F12 = 65
SID_SOFTWARE_F13 = 66
SID_SOFTWARE_F14 = 67
SID_SOFTWARE_F15 = 68
SID_SOFTWARE_F16 = 69
function_key_control_switch_ids = range(SID_SOFTWARE_F1, SID_SOFTWARE_F16 + 1)
SID_MOD_SHIFT = 70
SID_MOD_OPTION = 71
SID_MOD_CTRL = 72
SID_MOD_ALT = 73
SID_AUTOMATION_ON = 74
SID_AUTOMATION_RECORD = 75
SID_AUTOMATION_SNAPSHOT = 77
SID_AUTOMATION_TOUCH = 78
SID_FUNC_UNDO = 76
SID_FUNC_CANCEL = 80
SID_FUNC_ENTER = 81
SID_FUNC_REDO = 79
SID_FUNC_MARKER = 82
SID_FUNC_MIXER = 83
software_controls_switch_ids = (
 SID_MOD_SHIFT,
 SID_MOD_OPTION,
 SID_MOD_CTRL,
 SID_MOD_ALT,
 SID_AUTOMATION_ON,
 SID_AUTOMATION_RECORD,
 SID_AUTOMATION_SNAPSHOT,
 SID_AUTOMATION_TOUCH,
 SID_FUNC_UNDO,
 SID_FUNC_CANCEL,
 SID_FUNC_ENTER,
 SID_FUNC_REDO,
 SID_FUNC_MARKER,
 SID_FUNC_MIXER)
SID_TRANSPORT_REWIND = 91
SID_TRANSPORT_FAST_FORWARD = 92
SID_TRANSPORT_STOP = 93
SID_TRANSPORT_PLAY = 94
SID_TRANSPORT_RECORD = 95
transport_control_switch_ids = range(SID_TRANSPORT_REWIND, SID_TRANSPORT_RECORD + 1)
SID_MARKER_FROM_PREV = 84
SID_MARKER_FROM_NEXT = 85
SID_MARKER_LOOP = 86
SID_MARKER_PI = 87
SID_MARKER_PO = 88
SID_MARKER_HOME = 89
SID_MARKER_END = 90
marker_control_switch_ids = (
 SID_MARKER_FROM_PREV,
 SID_MARKER_FROM_NEXT,
 SID_MARKER_LOOP,
 SID_MARKER_PI,
 SID_MARKER_PO,
 SID_MARKER_HOME,
 SID_MARKER_END)
SID_JOG_CURSOR_UP = 96
SID_JOG_CURSOR_DOWN = 97
SID_JOG_CURSOR_LEFT = 98
SID_JOG_CURSOR_RIGHT = 99
SID_JOG_ZOOM = 100
SID_JOG_SCRUB = 101
jog_wheel_switch_ids = range(SID_JOG_CURSOR_UP, SID_JOG_SCRUB + 1)
SID_USER_FOOT_SWITCHA = 102
SID_USER_FOOT_SWITCHB = 103
SID_FADER_TOUCH_SENSE_BASE = 104
SID_FADER_TOUCH_SENSE_CH1 = 104
SID_FADER_TOUCH_SENSE_CH2 = 105
SID_FADER_TOUCH_SENSE_CH3 = 106
SID_FADER_TOUCH_SENSE_CH4 = 107
SID_FADER_TOUCH_SENSE_CH5 = 108
SID_FADER_TOUCH_SENSE_CH6 = 109
SID_FADER_TOUCH_SENSE_CH7 = 110
SID_FADER_TOUCH_SENSE_CH8 = 111
SID_FADER_TOUCH_SENSE_MASTER = 112
fader_touch_switch_ids = range(SID_FADER_TOUCH_SENSE_CH1, SID_FADER_TOUCH_SENSE_MASTER + 1)
SID_LAST = 112