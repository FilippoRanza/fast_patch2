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


import random
rnd = random.SystemRandom()

DEF_MAX_LEN = 64
DEF_MIN_LEN = 4

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
         'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
         '4', '5', '6', '7', '8', '9', '_', '-']

rnd.shuffle(chars)
len_chars = len(chars)


def rand_int(a, b=None):
    if b is None:
        b = a
        a = 0
    return rnd.randint(a, b)


def _mk_rnd_str_(sz):
    out = ''
    for i in range(sz):
        tmp = rand_int(len_chars - 1)
        out += chars[tmp]
    return out


def rand_str(sz=None):
    if sz is None:
        sz = rand_int(DEF_MIN_LEN, DEF_MAX_LEN)
    return _mk_rnd_str_(sz)


def rand_state(c):
    a = rnd.random()
    j = 1 / c
    state = j
    for i in range(c):
        if a < state:
            return i
        state += j
    return c - 1

