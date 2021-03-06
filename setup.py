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

from sys import version_info

from setuptools import setup

from find_script import find_script

# you can't install with python2
assert version_info >= (3, 6), 'fast_patch2 needs python 3.6 or greater'


setup(
    name='fast_patch2',
    version='0.1',
    packages=['file_utils', 'line_refactor'],
    url='https://github.com/FilippoRanza/fast_patch2',
    license='GPL3',
    author='Filippo Ranza',
    author_email='filipporanza@gmail.com',
    description='Automatically refactor Latex code',
    scripts=find_script()
)
