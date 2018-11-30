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
check that the installation script works properly
"""

from subprocess import call

from find_script import find_script

_ERROR_ = -1


def check_installation(f):
    try:
        a = call(f)
    except FileNotFoundError:
        print(f, 'not found')
        a = _ERROR_
    except PermissionError:
        print(f, 'is not executable')
        a = _ERROR_

    return a


def test():
    for f in find_script():
        assert check_installation(f) != _ERROR_




