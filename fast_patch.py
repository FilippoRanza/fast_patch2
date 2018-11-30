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


from file_utils import Inplace, find_files
from line_refactor import refactor_line, reset_refactor
from argparse import ArgumentParser


def init_arg_parse():
    parse = ArgumentParser()
    # parse.add_argument('-l', '--label', default=False, action='store_true',
    #                   help='Automatically add label under section and chapter, when a label is missing')

    group = parse.add_argument_group().add_mutually_exclusive_group()
    group.add_argument('-a', '--auto', action='store_true',
                       help='Automatically locate *tex file in current directory and all its subdirectories')

    group.add_argument('-f', '--file', nargs='+', type=str,
                       help='Input file to refactor')

    return parse


def run_config(args):
    if args.auto:
        args.file = find_files()

    return args


def refactor_file(file_name, bak):
    with Inplace(file_name, bak) as f:
        for l in f:
            tmp = refactor_line(l)
            f.write(tmp)

    reset_refactor()


def main():
    # refactor_file('test.tex', 'bak')
    parse = init_arg_parse()
    args = run_config(parse.parse_args())
    for f in args.file:
        refactor_file(f, 'bak')


if __name__ == '__main__':
    main()




