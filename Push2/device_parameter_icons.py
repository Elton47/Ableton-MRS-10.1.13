# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/device_parameter_icons.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
IMAGE_ID_TO_FILENAME = {'amp_bass': (u'amp_bass.svg', u''), 
   'amp_blues': (u'amp_blues.svg', u''), 
   'amp_boost': (u'amp_boost.svg', u''), 
   'amp_clean': (u'amp_clean.svg', u''), 
   'amp_heavy': (u'amp_heavy.svg', u''), 
   'amp_lead': (u'amp_lead.svg', u''), 
   'amp_rock': (u'amp_rock.svg', u''), 
   'armed': (u'armed.svg', u''), 
   'cabinet_1x12': (u'cabinet_1x12.svg', u''), 
   'cabinet_2x12': (u'cabinet_2x12.svg', u''), 
   'cabinet_4x10': (u'cabinet_4x10.svg', u''), 
   'cabinet_4x10bass': (u'cabinet_4x10bass.svg', u''), 
   'cabinet_4x12': (u'cabinet_4x12.svg', u''), 
   'cancel_x': (u'cancel_x.svg', u''), 
   'circuit_clean': (u'circuit_clean.svg', u''), 
   'circuit_ms2': (u'circuit_ms2.svg', u''), 
   'circuit_osr': (u'circuit_osr.svg', u''), 
   'circuit_prd': (u'circuit_prd.svg', u''), 
   'circuit_smp': (u'circuit_smp.svg', u''), 
   'co_beam': (u'co_beam.svg', u''), 
   'co_marimba': (u'co_marimba.svg', u''), 
   'co_membrane': (u'co_membrane.svg', u''), 
   'co_pipe': (u'co_pipe.svg', u''), 
   'co_plate': (u'co_plate.svg', u''), 
   'co_string': (u'co_string.svg', u''), 
   'co_tube': (u'co_tube.svg', u''), 
   'compressor_expand': (u'compressor_expand.svg', u''), 
   'compressor_peak': (u'compressor_peak.svg', u''), 
   'compressor_rms': (u'compressor_rms.svg', u''), 
   'control_off': (u'control_off.svg', u''), 
   'control_on': (u'control_on.svg', u''), 
   'delay_16th_1': (u'delay_16th_1.svg', u''), 
   'delay_16th_2': (u'delay_16th_2.svg', u''), 
   'delay_16th_3': (u'delay_16th_3.svg', u''), 
   'delay_16th_4': (u'delay_16th_4.svg', u''), 
   'delay_16th_5': (u'delay_16th_5.svg', u''), 
   'delay_16th_6': (u'delay_16th_6.svg', u''), 
   'delay_16th_8': (u'delay_16th_8.svg', u''), 
   'delay_16th_16': (u'delay_16th_16.svg', u''), 
   'delay_pingping_on': (u'delay_pingping_on.svg', u''), 
   'delay_pingping_off': (u'delay_pingping_off.svg', u''), 
   'device_pad': (u'device_pad.svg', u''), 
   'device_rack_drum': (u'device_rack_drum.svg', u''), 
   'device_rack_effect': (u'device_rack_effect.svg', u''), 
   'device_rack_instrument': (u'device_rack_instrument.svg', u''), 
   'drumbuss_soft': (u'drumbuss_soft.svg', u''), 
   'drumbuss_medium': (u'drumbuss_medium.svg', u''), 
   'drumbuss_hard': (u'drumbuss_hard.svg', u''), 
   'echo_16th': (u'echo_16th.svg', u''), 
   'echo_dotted': (u'echo_dotted.svg', u''), 
   'echo_note': (u'echo_note.svg', u''), 
   'echo_triplet': (u'echo_triplet.svg', u''), 
   'eq8_band1': (u'eq8_band1.svg', u''), 
   'eq8_band2': (u'eq8_band2.svg', u''), 
   'eq8_band3': (u'eq8_band3.svg', u''), 
   'eq8_band4': (u'eq8_band4.svg', u''), 
   'eq8_band5': (u'eq8_band5.svg', u''), 
   'eq8_band6': (u'eq8_band6.svg', u''), 
   'eq8_band7': (u'eq8_band7.svg', u''), 
   'eq8_band8': (u'eq8_band8.svg', u''), 
   'filter_band_12': (u'filter_band_12.svg', u'12BandPass_small.svg'), 
   'filter_band_24': (u'filter_band_24.svg', u'24BandPass_small.svg'), 
   'filter_band_6': (u'filter_band_6.svg', u''), 
   'filter_band_ladr': (u'filter_band_ladr.svg', u''), 
   'filter_band_ms2': (u'filter_band_ms2.svg', u''), 
   'filter_band_osr': (u'filter_band_osr.svg', u''), 
   'filter_band_prd': (u'filter_band_prd.svg', u''), 
   'filter_band_svf': (u'filter_band_svf.svg', u''), 
   'filter_bell': (u'filter_bell.svg', u'Bell_small.svg'), 
   'filter_formant_12': (u'filter_formant_12.svg', u''), 
   'filter_formant_6': (u'filter_formant_6.svg', u''), 
   'filter_high_12': (u'filter_high_12.svg', u'12HighPass_small.svg'), 
   'filter_high_24': (u'filter_high_24.svg', u'24HighPass_small.svg'), 
   'filter_high_48': (u'filter_high_48.svg', u'24HighPass_small.svg'), 
   'filter_high_ladr': (u'filter_high_ladr.svg', u''), 
   'filter_high_ms2': (u'filter_high_ms2.svg', u''), 
   'filter_high_osr': (u'filter_high_osr.svg', u''), 
   'filter_high_prd': (u'filter_high_prd.svg', u''), 
   'filter_high_shelf': (u'filter_high_shelf.svg', u'HighShelf_small.svg'), 
   'filter_high_svf': (u'filter_high_svf.svg', u''), 
   'filter_low_12': (u'filter_low_12.svg', u'12LowPass_small.svg'), 
   'filter_low_24': (u'filter_low_24.svg', u'24LowPass_small.svg'), 
   'filter_low_48': (u'filter_low_24.svg', u'24LowPass_small.svg'), 
   'filter_low_ladr': (u'filter_low_ladr.svg', u''), 
   'filter_low_ms2': (u'filter_low_ms2.svg', u''), 
   'filter_low_osr': (u'filter_low_osr.svg', u''), 
   'filter_low_prd': (u'filter_low_prd.svg', u''), 
   'filter_low_shelf': (u'filter_low_shelf.svg', u'LowShelf_small.svg'), 
   'filter_low_svf': (u'filter_low_svf.svg', u''), 
   'filter_morph_12': (u'filter_morph_12.svg', u'12Morph_small.svg'), 
   'filter_morph_24': (u'filter_morph_24.svg', u'24Morph_small.svg'), 
   'filter_notch_12': (u'filter_notch_12.svg', u'12Notch_small.svg'), 
   'filter_notch_24': (u'filter_notch_24.svg', u'24Notch_small.svg'), 
   'icon_horizontal1': (u'icon_horizontal1.svg', u''), 
   'icon_horizontal15': (u'icon_horizontal15.svg', u''), 
   'lfo_free': (u'lfo_free.svg', u''), 
   'lfo_phase': (u'lfo_phase.svg', u''), 
   'lfo_spin': (u'lfo_spin.svg', u''), 
   'lfo_sync': (u'lfo_sync.svg', u''), 
   'lfo_sine_small': (u'', u'lfo_sine_small.svg'), 
   'lfo_triangle_small': (u'', u'lfo_triangle_small.svg'), 
   'lfo_saw_up_small': (u'', u'lfo_saw_up_small.svg'), 
   'lfo_saw_down_small': (u'', u'lfo_saw_down_small.svg'), 
   'lfo_square_small': (u'', u'lfo_square_small.svg'), 
   'lfo_random_small': (u'', u'lfo_random_small.svg'), 
   'mic_condenser': (u'mic_condenser.svg', u''), 
   'mic_dynamic': (u'mic_dynamic.svg', u''), 
   'mic_far': (u'mic_far.svg', u''), 
   'mic_nearoff': (u'mic_nearoff.svg', u''), 
   'mic_nearon': (u'mic_nearon.svg', u''), 
   'osc_a': (u'osc_a.svg', u''), 
   'osc_alg_1': (u'osc_alg_1.svg', u''), 
   'osc_alg_10': (u'osc_alg_10.svg', u''), 
   'osc_alg_11': (u'osc_alg_11.svg', u''), 
   'osc_alg_2': (u'osc_alg_2.svg', u''), 
   'osc_alg_3': (u'osc_alg_3.svg', u''), 
   'osc_alg_4': (u'osc_alg_4.svg', u''), 
   'osc_alg_5': (u'osc_alg_5.svg', u''), 
   'osc_alg_6': (u'osc_alg_6.svg', u''), 
   'osc_alg_7': (u'osc_alg_7.svg', u''), 
   'osc_alg_8': (u'osc_alg_8.svg', u''), 
   'osc_alg_9': (u'osc_alg_9.svg', u''), 
   'osc_b': (u'osc_b.svg', u''), 
   'osc_c': (u'osc_c.svg', u''), 
   'osc_d': (u'osc_d.svg', u''), 
   'pedal_distortion': (u'pedal_distortion.svg', u''), 
   'pedal_fuzz': (u'pedal_fuzz.svg', u''), 
   'pedal_overdrive': (u'pedal_overdrive.svg', u''), 
   'phase_inverted': (u'phase_inverted.svg', u''), 
   'phase_normal': (u'phase_normal.svg', u''), 
   'route_in': (u'route_in.svg', u''), 
   'route_out': (u'route_out.svg', u''), 
   'simpler_1shot': (u'simpler_1shot.svg', u''), 
   'simpler_adsr': (u'simpler_adsr.svg', u''), 
   'simpler_slice': (u'simpler_slice.svg', u''), 
   'tension_bow': (u'tension_bow.svg', u''), 
   'tension_hammer': (u'tension_hammer.svg', u''), 
   'tension_hammerbounce': (u'tension_hammerbounce.svg', u''), 
   'tension_plectrum': (u'tension_plectrum.svg', u''), 
   'tension_plectum': (u'tension_plectum.svg', u''), 
   'track_group': (u'track_group.svg', u''), 
   'tube_a': (u'tube_a.svg', u''), 
   'utility_left': (u'utility_left.svg', u''), 
   'utility_right': (u'utility_right.svg', u''), 
   'utility_stereo': (u'utility_stereo.svg', u''), 
   'utility_swap': (u'utility_swap.svg', u''), 
   'tube_b': (u'tube_b.svg', u''), 
   'tube_c': (u'tube_c.svg', u''), 
   'voices_2': (u'voices_2.svg', u''), 
   'voices_3': (u'voices_3.svg', u''), 
   'voices_4': (u'voices_4.svg', u''), 
   'voices_5': (u'voices_5.svg', u''), 
   'voices_6': (u'voices_6.svg', u''), 
   'voices_7': (u'voices_7.svg', u''), 
   'voices_8': (u'voices_8.svg', u''), 
   'wave_noise_loop': (u'wave_noise_loop.svg', u''), 
   'wave_noise_white': (u'wave_noise_white.svg', u''), 
   'wave_saw_16': (u'wave_saw_16.svg', u''), 
   'wave_saw_3': (u'wave_saw_3.svg', u''), 
   'wave_saw_32': (u'wave_saw_32.svg', u''), 
   'wave_saw_4': (u'wave_saw_4.svg', u''), 
   'wave_saw_6': (u'wave_saw_6.svg', u''), 
   'wave_saw_64': (u'wave_saw_64.svg', u''), 
   'wave_saw_8': (u'wave_saw_8.svg', u''), 
   'wave_saw_down': (u'wave_saw_down.svg', u''), 
   'wave_saw_up': (u'wave_saw_up.svg', u''), 
   'wave_sh_mono': (u'wave_sh_mono.svg', u''), 
   'wave_sh_stereo': (u'wave_sh_stereo.svg', u''), 
   'wave_sine': (u'wave_sine.svg', u''), 
   'wave_sine_4bit': (u'wave_sine_4bit.svg', u''), 
   'wave_sine_8bit': (u'wave_sine_8bit.svg', u''), 
   'wave_square': (u'wave_square.svg', u''), 
   'wave_square_16': (u'wave_square_16.svg', u''), 
   'wave_square_3': (u'wave_square_3.svg', u''), 
   'wave_square_32': (u'wave_square_32.svg', u''), 
   'wave_square_4': (u'wave_square_4.svg', u''), 
   'wave_square_6': (u'wave_square_6.svg', u''), 
   'wave_square_64': (u'wave_square_64.svg', u''), 
   'wave_square_8': (u'wave_square_8.svg', u''), 
   'wave_triangle': (u'wave_triangle.svg', u''), 
   'wave_user': (u'wave_user.svg', u''), 
   'wavetable_effect_classic': (u'wavetable_effect_classic.svg', u''), 
   'wavetable_effect_fm': (u'wavetable_effect_fm.svg', u''), 
   'wavetable_effect_modern': (u'wavetable_effect_modern.svg', u''), 
   'wavetable_effect_none': (u'wavetable_effect_none.svg', u''), 
   'wavetable_env_loop': (u'wavetable_env_loop.svg', u''), 
   'wavetable_env_loop_none': (u'wavetable_env_loop_none.svg', u''), 
   'wavetable_env_loop_trigger': (u'wavetable_env_loop_trigger.svg', u''), 
   'wavetable_env_slope': (u'wavetable_env_slope.svg', u''), 
   'wavetable_env_time': (u'wavetable_env_time.svg', u''), 
   'wavetable_env_value': (u'wavetable_env_value.svg', u''), 
   'wavetable_filter_1': (u'', u'wavetable_filter_1_small.svg'), 
   'wavetable_filter_2': (u'', u'wavetable_filter_2_small.svg'), 
   'wavetable_filter_3': (u'', u'wavetable_filter_3_small.svg'), 
   'wavetable_filter_4': (u'', u'wavetable_filter_4_small.svg'), 
   'wavetable_filter_5': (u'', u'wavetable_filter_5_small.svg'), 
   'wavetable_filter_switch_1': (u'wavetable_filter_switch_1.svg', u''), 
   'wavetable_filter_switch_2': (u'wavetable_filter_switch_2.svg', u''), 
   'wavetable_octave_0': (u'wavetable_octave_0.svg', u''), 
   'wavetable_octave_minus_1': (u'wavetable_octave_minus_1.svg', u''), 
   'wavetable_octave_minus_2': (u'wavetable_octave_minus_2.svg', u''), 
   'wavetable_osc_1': (u'wavetable_osc_1.svg', u''), 
   'wavetable_osc_2': (u'wavetable_osc_2.svg', u''), 
   'wavetable_osc_mix': (u'wavetable_osc_mix.svg', u''), 
   'wavetable_osc_sub': (u'wavetable_osc_sub.svg', u''), 
   'wavetable_routing_parallel': (u'wavetable_routing_parallel.svg', u''), 
   'wavetable_routing_serial': (u'wavetable_routing_serial.svg', u''), 
   'wavetable_routing_split': (u'wavetable_routing_split.svg', u''), 
   'wavetable_unison_classic': (u'wavetable_unison_classic.svg', u''), 
   'wavetable_unison_shimmer': (u'wavetable_unison_shimmer.svg', u''), 
   'wavetable_unison_noise': (u'wavetable_unison_noise.svg', u''), 
   'wavetable_unison_none': (u'wavetable_unison_none.svg', u''), 
   'wavetable_unison_phase_sync': (u'wavetable_unison_phase_sync.svg', u''), 
   'wavetable_unison_position_spread': (u'wavetable_unison_position_spread.svg', u''), 
   'wavetable_unison_random': (u'wavetable_unison_random.svg', u''), 
   'workflow_clip': (u'workflow_clip.svg', u''), 
   'workflow_scene': (u'workflow_scene.svg', u'')}
OPERATOR_OSCILLATORS = (u'wave_sine', u'wave_sine_4bit', u'wave_sine_8bit', u'wave_saw_3',
                        u'wave_saw_4', u'wave_saw_6', u'wave_saw_8', u'wave_saw_16',
                        u'wave_saw_32', u'wave_saw_64', u'wave_saw_down', u'wave_square_3',
                        u'wave_square_4', u'wave_square_6', u'wave_square_8', u'wave_square_16',
                        u'wave_square_32', u'wave_square_64', u'wave_square', u'wave_triangle',
                        u'wave_noise_loop', u'wave_noise_white', u'wave_user')
ACTIVATE = (u'control_off', u'control_on')
ANALOG_OSCILLATORS = (u'wave_sine', u'wave_saw_down', u'wave_square', u'wave_noise_white')
ANALOG_L_F_O = (u'wave_sine', u'wave_triangle', u'wave_square', u'wave_noise_white',
                u'wave_noise_white')
ANALOG_FILTERS = (u'filter_low_12', u'filter_low_24', u'filter_band_6', u'filter_band_12',
                  u'filter_notch_12', u'filter_notch_24', u'filter_high_12', u'filter_high_24',
                  u'filter_formant_6', u'filter_formant_12')
RESONANCE_TYPES = (u'co_beam', u'co_marimba', u'co_string', u'co_membrane', u'co_plate',
                   u'co_pipe', u'co_tube')
COLLISION_FILTERS = (u'filter_low_12', u'filter_high_12', u'filter_band_12', u'filter_band_6')
COLLISION_L_F_O = (u'wave_sine', u'wave_square', u'wave_triangle', u'wave_saw_up',
                   u'wave_saw_down', u'wave_sh_mono', u'wave_noise_white')
IMPULSE_FILTERS = (u'filter_low_12', u'filter_low_24', u'filter_band_12', u'filter_band_24',
                   u'filter_high_12', u'filter_high_24', u'filter_notch_12')
SAMPLER_OSCILLATORS = (u'wave_sine', u'wave_square', u'wave_triangle', u'wave_saw_up',
                       u'wave_saw_down', u'wave_sh_mono')
LFO_WAVEFORMS = (u'wave_sine', u'wave_square', u'wave_triangle', u'wave_saw_up', u'wave_saw_down',
                 u'wave_sh_stereo', u'wave_sh_mono')
STEREO_MODE = (u'lfo_phase', u'lfo_spin')
SYNC = (u'lfo_free', u'lfo_sync')
EQ8_FILTER_TYPES = (u'filter_high_48', u'filter_high_12', u'filter_low_shelf', u'filter_bell',
                    u'filter_notch_24', u'filter_high_shelf', u'filter_low_12', u'filter_low_48')
CYTOMIC_FILTER_TYPES = (u'filter_low_48', u'filter_high_48', u'filter_band_24', u'filter_notch_24',
                        u'filter_morph_24')
FILTER_CIRCUIT_TYPES = (u'circuit_clean', u'circuit_osr', u'circuit_ms2', u'circuit_smp',
                        u'circuit_prd')
COMPRESSOR_MODES = (u'compressor_peak', u'compressor_rms', u'compressor_expand')
WAVETABLE_LOOP_MODE = (u'wavetable_env_loop_none', u'wavetable_env_loop_trigger', u'wavetable_env_loop')
WAVETABLE_OSCILLATOR_SWITCH = (u'wavetable_osc_1', u'wavetable_osc_2', u'wavetable_osc_sub',
                               u'wavetable_osc_mix')
WAVETABLE_OSCILLATOR_EFFECT_TYPES = (u'wavetable_effect_none', u'wavetable_effect_fm',
                                     u'wavetable_effect_classic', u'wavetable_effect_modern')
WAVETABLE_FILTER_TYPES = (u'wavetable_filter_1', u'wavetable_filter_2', u'wavetable_filter_3',
                          u'wavetable_filter_4', u'wavetable_filter_5')
WAVETABLE_LFO_TYPES = (u'lfo_sine_small', u'lfo_triangle_small', u'lfo_saw_down_small',
                       u'lfo_square_small', u'lfo_random_small')
WAVETABLE_VOICES = (u'voices_2', u'voices_3', u'voices_4', u'voices_5', u'voices_6',
                    u'voices_7', u'voices_8')
GENERIC_PARAMETER_IMAGES = {'LFO Waveform': LFO_WAVEFORMS, 
   'Waveform': (u'wave_sine', u'wave_triangle', u'wave_saw_down', u'wave_sh_stereo'), 
   'Filter Type': (u'filter_low_48', u'filter_high_48', u'filter_band_24', u'filter_notch_24'), 
   'Ext. In On': ACTIVATE, 
   'LFO Sync': SYNC, 
   'Sync': SYNC, 
   'Adaptive Q': ACTIVATE, 
   'LFO Stereo Mode': STEREO_MODE, 
   'Side Listen': ACTIVATE, 
   'EQ On': ACTIVATE, 
   'EQ Mode': (u'filter_low_shelf', u'filter_bell', u'filter_high_shelf', u'filter_low_48', u'filter_band_24',
 u'filter_high_48')}
DEVICE_PARAMETER_IMAGES = {'UltraAnalog': {'OSC1 On/Off': ACTIVATE, 
                   'OSC2 On/Off': ACTIVATE, 
                   'F1 On/Off': ACTIVATE, 
                   'F2 On/Off': ACTIVATE, 
                   'AMP1 On/Off': ACTIVATE, 
                   'AMP2 On/Off': ACTIVATE, 
                   'Noise On/Off': ACTIVATE, 
                   'Unison On/Off': ACTIVATE, 
                   'Glide On/Off': ACTIVATE, 
                   'Glide Legato': ACTIVATE, 
                   'LFO1 On/Off': ACTIVATE, 
                   'LFO1 Sync': SYNC, 
                   'LFO2 On/Off': ACTIVATE, 
                   'LFO2 Sync': SYNC, 
                   'F1 On/Off': ACTIVATE, 
                   'F2 On/Off': ACTIVATE, 
                   'Vib On/Off': ACTIVATE, 
                   'OSC1 Shape': ANALOG_OSCILLATORS, 
                   'OSC2 Shape': ANALOG_OSCILLATORS, 
                   'F1 Type': ANALOG_FILTERS, 
                   'F2 Type': ANALOG_FILTERS, 
                   'LFO1 Shape': ANALOG_L_F_O, 
                   'LFO2 Shape': ANALOG_L_F_O}, 
   'ChannelEq': {'Highpass On': ACTIVATE}, 'Collision': {'Res 1 Type': RESONANCE_TYPES, 
                 'Res 2 Type': RESONANCE_TYPES, 
                 'Mallet On/Off': ACTIVATE, 
                 'Noise On/Off': ACTIVATE, 
                 'Res 1 On/Off': ACTIVATE, 
                 'Res 2 On/Off': ACTIVATE, 
                 'LFO 1 On/Off': ACTIVATE, 
                 'LFO 2 On/Off': ACTIVATE, 
                 'Mallet On/Off': ACTIVATE, 
                 'Noise Filter Type': COLLISION_FILTERS, 
                 'LFO 1 Shape': COLLISION_L_F_O, 
                 'LFO 2 Shape': COLLISION_L_F_O, 
                 'LFO 1 Sync': SYNC, 
                 'LFO 2 Sync': SYNC}, 
   'InstrumentImpulse': {'1 Filter Type': IMPULSE_FILTERS, 
                         '2 Filter Type': IMPULSE_FILTERS, 
                         '3 Filter Type': IMPULSE_FILTERS, 
                         '4 Filter Type': IMPULSE_FILTERS, 
                         '5 Filter Type': IMPULSE_FILTERS, 
                         '6 Filter Type': IMPULSE_FILTERS, 
                         '7 Filter Type': IMPULSE_FILTERS, 
                         '8 Filter Type': IMPULSE_FILTERS}, 
   'StringStudio': {'Excitator Type': (u'tension_bow', u'tension_hammer', u'tension_hammerbounce', u'tension_plectrum'), 
                    'Filter Type': (u'filter_low_12', u'filter_low_24', u'filter_band_6', u'filter_band_12', u'filter_notch_12',
 u'filter_notch_24', u'filter_high_12', u'filter_high_24', u'filter_formant_6', u'filter_formant_12'), 
                    'Exc On/Off': ACTIVATE, 
                    'E Pos Abs': ACTIVATE, 
                    'Pickup On/Off': ACTIVATE, 
                    'Damper On': ACTIVATE, 
                    'Damper Gated': ACTIVATE, 
                    'D Pos Abs': ACTIVATE, 
                    'Term On/Off': ACTIVATE, 
                    'Body On/Off': ACTIVATE, 
                    'Filter On/Off': ACTIVATE, 
                    'LFO On/Off': ACTIVATE, 
                    'Vibrato On/Off': ACTIVATE, 
                    'Unison On/Off': ACTIVATE, 
                    'Porta On/Off': ACTIVATE, 
                    'Porta Legato': ACTIVATE, 
                    'Porta Prop': ACTIVATE, 
                    'FEG On/Off': ACTIVATE, 
                    'Damper Gated': ACTIVATE, 
                    'LFO Sync On': SYNC, 
                    'LFO Shape': (u'wave_sine', u'wave_triangle', u'wave_square', u'wave_sh_mono', u'wave_noise_white')}, 
   'Operator': {'Oscillator': (u'osc_a', u'osc_b', u'osc_c', u'osc_d'), 
                'Algorithm': (u'osc_alg_1', u'osc_alg_2', u'osc_alg_3', u'osc_alg_4', u'osc_alg_5', u'osc_alg_6',
 u'osc_alg_7', u'osc_alg_8', u'osc_alg_9', u'osc_alg_10', u'osc_alg_11'), 
                'Filter Type': CYTOMIC_FILTER_TYPES, 
                'Filter Circuit - LP/HP': FILTER_CIRCUIT_TYPES, 
                'Filter Circuit - BP/NO/Morph': FILTER_CIRCUIT_TYPES, 
                'LFO Type': (u'wave_sine', u'wave_square', u'wave_triangle', u'wave_saw_up', u'wave_saw_down',
 u'wave_sh_mono', u'wave_noise_white'), 
                'Osc-A Wave': OPERATOR_OSCILLATORS, 
                'Osc-B Wave': OPERATOR_OSCILLATORS, 
                'Osc-C Wave': OPERATOR_OSCILLATORS, 
                'Osc-D Wave': OPERATOR_OSCILLATORS, 
                'Filter On': ACTIVATE, 
                'Osc-A On': ACTIVATE, 
                'A Quantize': ACTIVATE, 
                'B Quantize': ACTIVATE, 
                'C Quantize': ACTIVATE, 
                'D Quantize': ACTIVATE, 
                'Osc-A Retrig': ACTIVATE, 
                'A Fix On ': ACTIVATE, 
                'Osc-B On': ACTIVATE, 
                'Osc-B Quantize': ACTIVATE, 
                'Osc-B Retrig': ACTIVATE, 
                'B Fix On ': ACTIVATE, 
                'Osc-C On': ACTIVATE, 
                'Osc-C Quantize': ACTIVATE, 
                'Osc-C Retrig': ACTIVATE, 
                'C Fix On ': ACTIVATE, 
                'Osc-D On': ACTIVATE, 
                'Osc-D Quantize': ACTIVATE, 
                'Osc-D Retrig': ACTIVATE, 
                'D Fix On ': ACTIVATE, 
                'LFO On': ACTIVATE, 
                'LFO Retrigger': ACTIVATE, 
                'Glide On': ACTIVATE, 
                'Pe On': ACTIVATE, 
                'LFO < Pe': ACTIVATE, 
                'Osc-A < Pe': ACTIVATE, 
                'Osc-B < Pe': ACTIVATE, 
                'Osc-C < Pe': ACTIVATE, 
                'Osc-D < Pe': ACTIVATE, 
                'Filt < LFO': ACTIVATE, 
                'Osc-A < LFO': ACTIVATE, 
                'Osc-B < LFO': ACTIVATE, 
                'Osc-C < LFO': ACTIVATE, 
                'Osc-D < LFO': ACTIVATE}, 
   'MultiSampler': {'F On': ACTIVATE, 
                    'Fe On': ACTIVATE, 
                    'Shaper On': ACTIVATE, 
                    'Osc On': ACTIVATE, 
                    'O Fix On': ACTIVATE, 
                    'O Type': OPERATOR_OSCILLATORS, 
                    'Pe On': ACTIVATE, 
                    'L 1 On': ACTIVATE, 
                    'L 1 Sync': SYNC, 
                    'L 1 Retrig': ACTIVATE, 
                    'L 1 Wave': SAMPLER_OSCILLATORS, 
                    'L 2 On': ACTIVATE, 
                    'L 2 Sync': SYNC, 
                    'L 2 St Mode': STEREO_MODE, 
                    'L 2 Retrig': ACTIVATE, 
                    'L 2 Wave': SAMPLER_OSCILLATORS, 
                    'L 3 On': ACTIVATE, 
                    'L 3 Sync': SYNC, 
                    'L 3 St Mode': STEREO_MODE, 
                    'L 3 Retrig': ACTIVATE, 
                    'L 3 Wave': SAMPLER_OSCILLATORS, 
                    'Ae On': ACTIVATE, 
                    'Filter Type': CYTOMIC_FILTER_TYPES, 
                    'Filter Circuit - LP/HP': FILTER_CIRCUIT_TYPES, 
                    'Filter Circuit - BP/NO/Morph': FILTER_CIRCUIT_TYPES}, 
   'OriginalSimpler': {'F On': ACTIVATE, 
                       'Fe On': ACTIVATE, 
                       'L On': ACTIVATE, 
                       'L Retrig': ACTIVATE, 
                       'Pe On': ACTIVATE, 
                       'L Wave': (u'wave_sine', u'wave_square', u'wave_triangle', u'wave_saw_down', u'wave_saw_up',
 u'wave_sh_mono'), 
                       'Filter Type': CYTOMIC_FILTER_TYPES, 
                       'Filter Circuit - LP/HP': FILTER_CIRCUIT_TYPES, 
                       'Filter Circuit - BP/NO/Morph': FILTER_CIRCUIT_TYPES}, 
   'Amp': {'Amp Type': (u'amp_clean', u'amp_boost', u'amp_blues', u'amp_rock', u'amp_lead', u'amp_heavy',
 u'amp_bass'), 
           'Dual Mono': ACTIVATE}, 
   'AutoFilter': {'LFO Quantize On': ACTIVATE, 
                  'Filter Type': CYTOMIC_FILTER_TYPES, 
                  'Filter Circuit - LP/HP': FILTER_CIRCUIT_TYPES, 
                  'Filter Circuit - BP/NO/Morph': FILTER_CIRCUIT_TYPES}, 
   'AutoPan': {'Invert': (u'phase_normal', u'phase_inverted'), 
               'LFO Type': SYNC, 
               'Stereo Mode': STEREO_MODE}, 
   'BeatRepeat': {'Filter On': ACTIVATE, 'Repeat': ACTIVATE, 'Block Triplets': ACTIVATE}, 'Cabinet': {'Dual Mono': ACTIVATE, 
               'Cabinet Type': (u'cabinet_1x12', u'cabinet_2x12', u'cabinet_4x12', u'cabinet_4x10', u'cabinet_4x10bass'), 
               'Microphone Type': (u'mic_condenser', u'mic_dynamic'), 
               'Microphone Position': (u'mic_nearon', u'mic_nearoff', u'mic_far')}, 
   'Chorus': {'LFO Extend On': ACTIVATE, 'Link On': ACTIVATE}, 'Compressor2': {'Auto Release On/Off': ACTIVATE, 
                   'Makeup': ACTIVATE, 
                   'Model': COMPRESSOR_MODES}, 
   'Corpus': {'Resonance Type': RESONANCE_TYPES, 
              'LFO On/Off': ACTIVATE, 
              'LFO Shape': (u'wave_sine', u'wave_square', u'wave_triangle', u'wave_saw_up', u'wave_saw_down',
 u'wave_sh_mono', u'wave_noise_white'), 
              'LFO Stereo Mode': STEREO_MODE, 
              'MIDI Frequency': ACTIVATE, 
              'Note Off': ACTIVATE, 
              'Filter On/Off': ACTIVATE}, 
   'Delay': {'L 16th': (u'delay_16th_1', u'delay_16th_2', u'delay_16th_3', u'delay_16th_4', u'delay_16th_5',
 u'delay_16th_6', u'delay_16th_8', u'delay_16th_16'), 
             'R 16th': (u'delay_16th_1', u'delay_16th_2', u'delay_16th_3', u'delay_16th_4', u'delay_16th_5',
 u'delay_16th_6', u'delay_16th_8', u'delay_16th_16'), 
             'Channel': (u'utility_stereo', u'utility_left', u'utility_right'), 
             'Link Switch': (u'utility_stereo', u'utility_left'), 
             'L Sync Enum': SYNC, 
             'R Sync Enum': SYNC, 
             'Ping Pong': ACTIVATE}, 
   'DrumBuss': {'Drive Type': (u'drumbuss_soft', u'drumbuss_medium', u'drumbuss_hard')}, 'Tube': {'Tube Type': (u'tube_a', u'tube_b', u'tube_c')}, 'Echo': {'L Sync Mode': (u'echo_note', u'echo_triplet', u'echo_dotted', u'echo_16th'), 
            'R Sync Mode': (u'echo_note', u'echo_triplet', u'echo_dotted', u'echo_16th'), 
            'Mod Wave': (u'lfo_sine_small', u'lfo_triangle_small', u'lfo_saw_up_small', u'lfo_saw_down_small',
 u'lfo_square_small', u'lfo_random_small'), 
            'Link': ACTIVATE, 
            'Ping Pong': ACTIVATE, 
            'Repitch': ACTIVATE, 
            'Filter On': ACTIVATE, 
            'Mod Sync': ACTIVATE}, 
   'Eq8': {'Band': (u'eq8_band1', u'eq8_band2', u'eq8_band3', u'eq8_band4', u'eq8_band5', u'eq8_band6',
 u'eq8_band7', u'eq8_band8'), 
           '1 Filter Type A': EQ8_FILTER_TYPES, 
           '2 Filter Type A': EQ8_FILTER_TYPES, 
           '3 Filter Type A': EQ8_FILTER_TYPES, 
           '4 Filter Type A': EQ8_FILTER_TYPES, 
           '5 Filter Type A': EQ8_FILTER_TYPES, 
           '6 Filter Type A': EQ8_FILTER_TYPES, 
           '7 Filter Type A': EQ8_FILTER_TYPES, 
           '8 Filter Type A': EQ8_FILTER_TYPES, 
           '1 Filter On A': ACTIVATE, 
           '2 Filter On A': ACTIVATE, 
           '3 Filter On A': ACTIVATE, 
           '4 Filter On A': ACTIVATE, 
           '5 Filter On A': ACTIVATE, 
           '6 Filter On A': ACTIVATE, 
           '7 Filter On A': ACTIVATE, 
           '8 Filter On A': ACTIVATE}, 
   'FilterEQ3': {'LowOn': ACTIVATE, 'MidOn': ACTIVATE, 'HighOn': ACTIVATE}, 'FilterDelay': {'1 Input On': ACTIVATE, 
                   '2 Input On': ACTIVATE, 
                   '3 Input On': ACTIVATE, 
                   '1 Delay Mode': ACTIVATE, 
                   '2 Delay Mode': ACTIVATE, 
                   '3 Delay Mode': ACTIVATE}, 
   'FrequencyShifter': {'Wide': ACTIVATE, 'Drive On/Off': ACTIVATE}, 'GlueCompressor': {'Peak Clip In': ACTIVATE}, 'GrainDelay': {'Delay Mode': ACTIVATE}, 'InstrumentVector': {'Oscillator': WAVETABLE_OSCILLATOR_SWITCH, 
                        'Osc 1 Effect Type': WAVETABLE_OSCILLATOR_EFFECT_TYPES, 
                        'Osc 2 Effect Type': WAVETABLE_OSCILLATOR_EFFECT_TYPES, 
                        'Sub Transpose': (u'wavetable_octave_0', u'wavetable_octave_minus_1', u'wavetable_octave_minus_2'), 
                        'Filter': (u'wavetable_filter_switch_1', u'wavetable_filter_switch_2'), 
                        'Filter 1 Type': WAVETABLE_FILTER_TYPES, 
                        'Filter 2 Type': WAVETABLE_FILTER_TYPES, 
                        'Filter 1 On': ACTIVATE, 
                        'Filter 2 On': ACTIVATE, 
                        'Filter 1 LP/HP': FILTER_CIRCUIT_TYPES, 
                        'Filter 2 LP/HP': FILTER_CIRCUIT_TYPES, 
                        'Filter 1 BP/NO/Morph': FILTER_CIRCUIT_TYPES, 
                        'Filter 2 BP/NO/Morph': FILTER_CIRCUIT_TYPES, 
                        'Filter Routing': (u'wavetable_routing_serial', u'wavetable_routing_parallel', u'wavetable_routing_split'), 
                        'Amp Env View': (u'wavetable_env_time', u'wavetable_env_slope'), 
                        'Mod Env View': (u'wavetable_env_time', u'wavetable_env_slope', u'wavetable_env_value'), 
                        'Amp Loop Mode': WAVETABLE_LOOP_MODE, 
                        'Env 2 Loop Mode': WAVETABLE_LOOP_MODE, 
                        'Env 3 Loop Mode': WAVETABLE_LOOP_MODE, 
                        'LFO 1 Shape': WAVETABLE_LFO_TYPES, 
                        'LFO 2 Shape': WAVETABLE_LFO_TYPES, 
                        'LFO 1 Retrigger': ACTIVATE, 
                        'LFO 2 Retrigger': ACTIVATE, 
                        'Mono On': ACTIVATE, 
                        'Unison Mode': (u'wavetable_unison_none', u'wavetable_unison_classic', u'wavetable_unison_shimmer',
 u'wavetable_unison_noise', u'wavetable_unison_phase_sync', u'wavetable_unison_position_spread',
 u'wavetable_unison_random'), 
                        'Unison Voices': WAVETABLE_VOICES, 
                        'Poly Voices': WAVETABLE_VOICES}, 
   'Limiter': {'Auto': ACTIVATE, 'Link Channels': ACTIVATE}, 'Looper': {'Reverse': ACTIVATE}, 'MultibandDynamics': {'Band Activator (Low)': ACTIVATE, 
                         'Band Activator (Mid)': ACTIVATE, 
                         'Band Activator (High)': ACTIVATE, 
                         'Soft Knee On/Off': ACTIVATE}, 
   'Pedal': {'Type': (u'pedal_overdrive', u'pedal_distortion', u'pedal_fuzz'), 
             'Sub': ACTIVATE}, 
   'Redux': {'Bit On': ACTIVATE}, 'Resonator': {'Const': ACTIVATE, 
                 'Filter On': ACTIVATE, 
                 'I On': ACTIVATE, 
                 'II On': ACTIVATE, 
                 'III On': ACTIVATE, 
                 'IV On': ACTIVATE, 
                 'V On': ACTIVATE}, 
   'Reverb': {'In LowCut On': ACTIVATE, 
              'In HighCut On': ACTIVATE, 
              'ER Spin On': ACTIVATE, 
              'HiShelf On': ACTIVATE, 
              'LowShelf On': ACTIVATE, 
              'Freeze On': ACTIVATE, 
              'Flat On': ACTIVATE, 
              'Cut On': ACTIVATE, 
              'Chorus On': ACTIVATE}, 
   'Saturator': {'Color': ACTIVATE, 'Soft Clip': ACTIVATE}, 'StereoGain': {'Mute': ACTIVATE, 
                  'BlockDc': ACTIVATE, 
                  'Channel Mode': (u'utility_left', u'utility_stereo', u'utility_right', u'utility_swap'), 
                  'Left Inv': ACTIVATE, 
                  'Right Inv': ACTIVATE}, 
   'Vinyl': {'Tracing On': ACTIVATE, 'Pinch On': ACTIVATE}, 'Vocoder': {'Precise/Retro': ACTIVATE, 'Enhance': ACTIVATE}, 'MidiArpeggiator': {'Hold On': ACTIVATE, 
                       'Sync On': ACTIVATE, 
                       'Velocity On': ACTIVATE, 
                       'Vel. Retrigger': ACTIVATE}, 
   'MidiNoteLength': {'Trigger Mode': ACTIVATE, 'Sync On': ACTIVATE}, 'MidiRandom': {'Mode': ACTIVATE}, 'MidiScale': {'Fold': ACTIVATE}}

def get_image_filenames_from_ids(image_ids, small_images=False, image_id_to_filename=IMAGE_ID_TO_FILENAME):
    image_index = 1 if small_images else 0
    return [ image_id_to_filename.get(image_id, (u'', u''))[image_index] for image_id in image_ids
           ]


def get_image_filenames(parameter_name, device_type, small_images=False, device_parameter_images=DEVICE_PARAMETER_IMAGES, generic_parameter_images=GENERIC_PARAMETER_IMAGES, image_id_to_filename=IMAGE_ID_TO_FILENAME):
    image_ids = []
    if device_type in device_parameter_images and parameter_name in device_parameter_images[device_type]:
        image_ids = device_parameter_images[device_type][parameter_name]
    elif parameter_name in generic_parameter_images:
        image_ids = generic_parameter_images[parameter_name]
    return get_image_filenames_from_ids(image_ids, small_images=small_images, image_id_to_filename=image_id_to_filename)