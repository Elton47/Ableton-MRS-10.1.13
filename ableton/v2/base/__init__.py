# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/__init__.py
# Compiled at: 2020-01-09 15:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .dependency import DependencyError, depends, inject
from .disconnectable import CompoundDisconnectable, Disconnectable, disconnectable
from .event import Event, EventError, EventObject, MultiSlot, ObservablePropertyAlias, SerializableListenableProperties, Slot, SlotGroup, has_event, listenable_property, listens, listens_group
from .gcutil import histogram, instances_by_name, refget
from .isclose import isclose
from .live_api_utils import duplicate_clip_loop, is_parameter_bipolar, liveobj_changed, liveobj_valid
from .proxy import Proxy, ProxyBase
from .signal import Signal
from .util import Bindable, BooleanContext, NamedTuple, OutermostOnlyContext, Slicer, aggregate_contexts, chunks, clamp, compose, const, dict_diff, find_if, first, flatten, forward_property, get_slice, group, in_range, index_if, infinite_context_manager, instance_decorator, is_contextmanager, is_iterable, is_matrix, lazy_attribute, linear, maybe, memoize, mixin, monkeypatch, monkeypatch_extend, negate, next, nop, overlaymap, print_message, product, recursive_map, remove_if, second, sign, slice_size, slicer, third, to_slice, trace_value, union
__all__ = (
 'Bindable',
 'BooleanContext',
 'CompoundDisconnectable',
 'DependencyError',
 'Disconnectable',
 'Event',
 'EventError',
 'EventObject',
 'MultiSlot',
 'NamedTuple',
 'ObservablePropertyAlias',
 'OutermostOnlyContext',
 'Proxy',
 'ProxyBase',
 'SerializableListenableProperties',
 'Signal',
 'Slicer',
 'Slot',
 'SlotGroup',
 'aggregate_contexts',
 'chunks',
 'clamp',
 'compose',
 'const',
 'depends',
 'dict_diff',
 'disconnectable',
 'duplicate_clip_loop',
 'find_if',
 'first',
 'flatten',
 'forward_property',
 'get_slice',
 'group',
 'has_event',
 'histogram',
 'in_range',
 'index_if',
 'infinite_context_manager',
 'inject',
 'instance_decorator',
 'instances_by_name',
 'is_contextmanager',
 'is_iterable',
 'is_matrix',
 'is_parameter_bipolar',
 'isclose',
 'lazy_attribute',
 'linear',
 'listenable_property',
 'listens',
 'listens_group',
 'liveobj_changed',
 'liveobj_valid',
 'maybe',
 'memoize',
 'mixin',
 'monkeypatch',
 'monkeypatch_extend',
 'negate',
 'next',
 'nop',
 'overlaymap',
 'print_message',
 'product',
 'recursive_map',
 'refget',
 'remove_if',
 'second',
 'sign',
 'slice_size',
 'slicer',
 'third',
 'to_slice',
 'trace_value',
 'union')