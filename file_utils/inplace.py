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
#   This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


"""
Modify a file inplace:
    read from the original and write to a temp file
    then rename the temp file as the original and
    if needed create a backup copy of the original
"""

from shutil import move
from tempfile import NamedTemporaryFile


class Inplace:

    def __init__(self, name, bak=None):
        self.n_in = name
        self.bak = bak

    def __enter__(self):
        self.f_in = open(self.n_in)
        self.f_out = NamedTemporaryFile(delete=False)
        self.n_out = self.f_out.name
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f_in.close()
        self.f_out.close()

        if self.bak:
            tmp = f'{self.n_in}.{self.bak}'
            move(self.n_in, tmp)

        move(self.n_out, self.n_in)

    def __iter__(self):
        return self.f_in.readlines().__iter__()

    def write(self, line):
        tmp = bytearray(line.encode())
        self.f_out.write(tmp)
