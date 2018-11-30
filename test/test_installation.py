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

name = 'fast_patch.py'


def test():
    try:
        a = call(name)
    except FileNotFoundError:
        print(name, 'not found')
        a = -1
    except PermissionError:
        print(name, 'is not executable')
        a = -1

    # script execution will fail: the system is not configured
    assert a != -1




