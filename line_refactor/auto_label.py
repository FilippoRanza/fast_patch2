#! /usr/bin/python

#
#  fast_patch2 - Automatically refactor Latex code
#
#  Copyright (c) 2018 Filippo Ranza <filipporanza@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from ._common_ import *


def get_supported_words():
    return list(type_key.keys())


class AutoLabel:

    def __init__(self):
        self.prev = None

    def reset(self):
        self.prev = None

    def _add_label_(self, line):
        if label_re.match(line):
            return line
        tmp = f'\\label{{{self.prev}}}'
        return '\n'.join((tmp, line))

    def _get_label_(self, line):
        m = blocks_re.match(line)
        if m:
            t, n = m.groups()
            self.prev = f'{type_key[t]}:{n}'

    def refactor(self, line):
        if self.prev:
            line = self._add_label_(line)
            self.prev = None
        else:
            self._get_label_(line)
        return line

