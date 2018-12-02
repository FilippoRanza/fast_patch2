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


from re import compile

from .auto_label import AutoLabel
from .auto_reference import AutoReference
from .equation_refactor import EquationRefactor
from .indentation_refactor import IndentationRefactor


class LineRefactor:
    def __init__(self, **kwargs):
        self.cmt = compile(r'^\s*%.*')
        self.r = [EquationRefactor(), IndentationRefactor()]
        if kwargs.get('label'):
            self._add_refactor_(AutoLabel())

        if kwargs.get('ref'):
            self._add_refactor_(AutoReference())

    def _add_refactor_(self, obj):
        # insert in the second-last position
        tmp = len(self.r) - 1
        self.r.insert(tmp, obj)

    def refactor_line(self, line):

        # ignore empty lines and comments
        if not line or self.cmt.match(line):
            return line

        for r in self.r:
            line = r.refactor(line)
        return line

    def reset(self):
        for r in self.r:
            r.reset()


