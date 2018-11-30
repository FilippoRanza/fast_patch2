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

"""
Find .py files with a command line entry point
"""

import re
from os import chmod, stat
from os.path import relpath
from stat import S_IXUSR, S_IXGRP, S_IXOTH

from file_utils import find_files

_entry_point_ = re.compile(r"if\s+__name__\s*==\s*'__main__'\s*:\s*")


def _is_main_(file):
    with open(file) as f:
        for l in f:
            if _entry_point_.match(l):
                out = True
                break
        else:
            out = False
    return out


def _find_script_(r):
    for f in find_files(ext='py', recursive=r):
        if _is_main_(f):
            # get current mode and set executable bit
            curr = stat(f).st_mode
            chmod(f, curr | S_IXOTH | S_IXGRP | S_IXUSR)
            yield relpath(f)


def find_script(recursive=False):
    return list(_find_script_(recursive))

