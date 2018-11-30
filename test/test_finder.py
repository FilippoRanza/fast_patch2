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


"""
Automatically create some files and directories
then search them using finder
"""


from .random_utils import *
from random import choice
import os
from os import path
from tempfile import mkdtemp
from file_utils import find_files


class MakeRandFileTree:

    def __init__(self, base='.', steps=10000):
        self.steps = steps

        self.dir_db = {}
        self.curr = base

    def mk_rnd_file(self):
        if rand_bool():
            name = f'{rand_str()}.{rand_str()}'
        else:
            name = f'{rand_str()}.tex'
        full = path.join(self.curr, name)

        # just create an empty file
        with open(full, 'w'):
            pass

        self.dir_db[full] = False

    def mk_rnd_dir(self):
        name = rand_str()
        full = path.join(self.curr, name)
        os.mkdir(full)
        self.curr = os.getcwd()

    def rnd_cd(self):
        d = rand_int(len(self.dir_db))
        for i, v in enumerate(self.dir_db.keys()):
            if d == i:
                self.curr = path.dirname(v)
                break

    def run(self):
        for i in range(self.steps):
            f = choice([self.mk_rnd_dir, self.mk_rnd_file, self.rnd_cd])
            f()
        return self.dir_db


def test():
    new_dir = mkdtemp()
    os.chdir(new_dir)
    # base is set just to force a full qualified name
    a = MakeRandFileTree(base=new_dir, steps=10000)
    files = a.run()

    os.chdir(new_dir)
    # path is set just to force a full qualified name
    for f in find_files(path=new_dir):
        files[f] = True

    for k, v in files.items():
        if k.endswith('.tex'):
            assert v
        else:
            assert not v















