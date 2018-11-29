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

from line_refactor.equation_refactor import EquationRefactor
from test.random_utils import *


def make_line():
    prev = ''
    curr = ''
    for i in range(rand_int(15)):
        s = rand_state(3)
        if s == 0:
            tmp = rand_str()
            prev += tmp
            curr += tmp
        elif s == 0:
            p = random.choice(['(', ')', '[', ']'])
            prev += p
            h = random.choice([r"\left", r"\right"])
            curr += f'{h}{p}'
        else:
            p = random.choice(['(', ')', '[', ']'])
            h = random.choice([r"\left", r"\right"])
            tmp = f'{h}{p}'
            prev += tmp
            curr += tmp

    return prev, curr


def make_rnd_block(name):
    if rand_state(2):
        n = random.choice(['equation', 'align'])
        change = True
    else:
        n = rand_str()
        change = False

    n += random.choice(['', '*'])

    head = ' ' * rand_int(5)
    tail = ' ' * rand_int(5)

    return f'{head}\\{name}{{{n}}}{tail}', change


def make_rnd_begin():
    return make_rnd_block('begin')


def make_rnd_end():
    return make_rnd_block('end')


def test_refactor():
    equation = EquationRefactor()
    for i in range(10000):
        prev, corr = make_line()

        s = rand_state(2)
        if s:
            equation.run = False
            assert prev == equation.refactor(prev)
        else:
            equation.run = False
            assert corr == equation.refactor(prev)


def run_begin(eq: EquationRefactor):
    line, ch = make_rnd_begin()
    prev = eq.run
    eq.refactor(line)
    if prev:
        assert eq.run
    else:
        assert eq.run == ch


def run_end(eq: EquationRefactor):
    line, ch = make_rnd_end()
    prev = eq.run
    eq.refactor(line)
    if prev:
        # if ch is True then line contains a correct end statement
        assert eq.run != ch
    else:
        assert not eq.run


def test_block():
    equation = EquationRefactor()
    for i in range(10000):
        f = random.choice([run_begin, run_end])
        f(equation)

