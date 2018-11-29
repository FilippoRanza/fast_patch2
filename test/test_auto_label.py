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

from random import choice

from line_refactor.auto_label import get_supported_words, AutoLabel
from .random_utils import *


def random_header(name):
    a, b = rand_surround()
    t = choice(get_supported_words())
    return f'{a}\\{t}{{{name}}}{b}'


def case_no_op(auto: AutoLabel):
    line = rand_str()
    assert auto.refactor(line) == line
    assert auto.prev is None


def case_add_label(auto: AutoLabel):
    name = rand_str()
    line = rand_str()

    curr = random_header(name)
    assert curr == auto.refactor(curr)
    assert auto.prev is not None

    curr = auto.refactor(line)
    label, tmp = curr.split('\n')
    assert auto.prev is None
    assert tmp == line


def case_no_add_label(auto: AutoLabel):
    name = rand_str()
    line = f'\\label{{{rand_str()}}}'

    curr = random_header(name)
    assert curr == auto.refactor(curr)
    assert auto.prev is not None

    curr = auto.refactor(line)
    assert auto.prev is None
    assert curr == line


def test():
    auto = AutoLabel()
    for i in range(10000):
        t = choice([case_add_label, case_no_add_label, case_no_op])
        t(auto)


