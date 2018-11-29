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
#  fast_patch2 - Automatically refactor Latex code
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import re

_begin_regex_ = re.compile(r'\s*\\begin\{.+\}\s*')
_end_regex_ = re.compile(r'\s*\\end\{.+\}\s*')


class IndentationRefactor:

    def __init__(self, indent='\t'):
        self.count = 0
        self.indent = indent

    def reset(self):
        self.count = 0

    def _indent_text_(self, txt):
        tmp = self.indent * self.count
        if txt.count('\n') == 1:
            out = tmp + txt.lstrip()
        else:
            # remove empty lines(for example if txt ends with \n)
            lines = filter(lambda x: x, txt.split('\n'))
            # add the previously removed line
            out = '\n'.join(map(lambda x: tmp + x.lstrip(), lines)) + '\n'
        return out

    def refactor(self, line: str):

        if _end_regex_.search(line):
            self.count -= 1

        if self.count:
            line = self._indent_text_(line)

        if _begin_regex_.search(line):
            self.count += 1

        return line


