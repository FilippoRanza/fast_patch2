#! /usr/bin/python

#
#  fast_patch2 - Automatically refactor Latex code
#
#   Copyright (c) 2018 Filippo Ranza <filipporanza@gmail.com>
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

from test.random_utils import *
from line_refactor.indentation_refactor import IndentationRefactor


def rand_statement(s):
    head = '' * rand_int(5)
    tail = '' * rand_int(5)
    cont = rand_str()
    return f'{head}\\{s}{{{cont}}}{tail}'


def rand_begin():
    return rand_statement('begin')


def rand_end():
    return rand_statement('end')


def test():
    indent = IndentationRefactor()
    k = 0
    for i in range(1000):
        s = rand_state(3)
        if s == 0:
            line = rand_str()
        elif s == 1:
            line = rand_begin()
            k += 1
        else:
            if k == 0:
                continue
            else:
                line = rand_end()
                k -= 1

        print(line, k)
        first = line[0]
        line = indent.refactor(line)
        assert k == indent.count

        # indentation after begin is incremented after line processing
        if s == 1:
            assert (k-1) == line.index(first)
        else:
            assert k == line.index(first)




