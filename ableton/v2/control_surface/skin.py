# uncompyle6 version 3.6.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/skin.py
# Compiled at: 2020-01-09 15:21:35
from __future__ import absolute_import, print_function, unicode_literals
from itertools import chain
from ableton.v2.base import depends, const, liveobj_valid, EventObject
from ableton.v2.control_surface.elements.color import is_dynamic_color_factory

class SkinColorMissingError(Exception):
    pass


class DynamicColorNotAvailableError(Exception):
    msg = 'In order to use dynamic colors, you need to inject the song while creating         the skin'


class Skin(EventObject):

    @depends(song=const(None))
    def __init__(self, colors=None, song=None, *a, **k):
        super(Skin, self).__init__(*a, **k)
        self._colors = {}
        self._factory_to_instance_map = {}
        if colors is not None:
            self._fill_colors(colors, song=song)
        return

    def _fill_colors(self, colors, pathname='', song=None):
        try:
            self._fill_colors(super(colors), song=song, pathname=pathname)
        except TypeError:
            for base in colors.__bases__:
                self._fill_colors(base, song=song, pathname=pathname)

        for k, v in colors.__dict__.iteritems():
            if k[:1] != '_':
                if callable(v):
                    self._fill_colors(v, pathname + k + '.', song=song)
                else:
                    if is_dynamic_color_factory(v):
                        v = self._get_dynamic_color(v, song)
                    self._colors[pathname + k] = v

    def __getitem__(self, key):
        try:
            return self._colors[key]
        except KeyError:
            raise SkinColorMissingError('Skin color missing: %s' % str(key))

    def iteritems(self):
        return self._colors.iteritems()

    def _get_dynamic_color(self, color_factory, song):
        if not liveobj_valid(song):
            raise DynamicColorNotAvailableError
        else:
            if color_factory not in self._factory_to_instance_map:
                self._factory_to_instance_map[color_factory] = self._create_dynamic_color(color_factory, song)
            return self._factory_to_instance_map[color_factory]

    def _create_dynamic_color(self, color_factory, song):
        return self.register_disconnectable(color_factory.instantiate(song))


def merge_skins(*skins):
    skin = Skin()
    skin._colors = dict(chain(*map(lambda s: s._colors.items(), skins)))
    return skin