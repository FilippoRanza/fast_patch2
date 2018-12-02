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

import re

from ._common_ import *

ref_re = re.compile('')


class AutoReference:

    def __init__(self):
        self.ref = {}

    def reset(self):
        self.ref.clear()

    def _store_token_(self, match):
        t, v = match.groups()
        tmp_k = re.compile(f'(?P<ref>{re.escape(v)})', re.IGNORECASE)
        tmp_v = f'\\g<ref>\\\\ref{{{type_key[t]}:{v}}}'
        self.ref[tmp_k] = tmp_v

    def _add_ref_(self, line):
        for k, v in self.ref.items():
            line = k.sub(v, line)
        return line

    def refactor(self, line: str):
        m = blocks_re.match(line)
        if m:
            self._store_token_(m)
        elif line.find('ref') == -1:
            line = self._add_ref_(line)

        return line

