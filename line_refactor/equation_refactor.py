#! /usr/bin/python

#
#  fast_patch - Automatically refactor Latex code
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

#
#  fast_patch - Automatically refactor Latex code
#
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

_begin_regex_ = re.compile(r'\\begin\{(align|equation)\*?\}')
_end_regex_ = re.compile(r'\\end\{(align|equation)\*?\}')

_parenthesis_refactor_ = [(re.compile(r'(\\left)?\('), r'\\left('),
                          (re.compile(r'(\\left)?\['), r'\\left['),
                          (re.compile(r'(\\right)?\)'), r'\\right)'),
                          (re.compile(r'(\\right)?\]'), r'\\right]')]


class EquationRefactor:

    def __init__(self):
        self.run = False

    @staticmethod
    def _refactor_(line):
        for r, s in _parenthesis_refactor_:
            line = r.sub(s, line)
        return line

    def refactor(self, line):

        if _end_regex_.search(line):
            self.run = False

        if self.run:
            line = self._refactor_(line)

        if _begin_regex_.search(line):
            self.run = True

        return line



