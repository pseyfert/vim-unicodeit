# Copyright (C) 2019 CERN for the benefit of the LHCb collaboration
# Author: Paul Seyfert <pseyfert@cern.ch>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import vim
import sys
import os

# to import the original unicodeit, the sys.path gets manipulated temporarily
# clean_syspath serves as a backup to restore a clean state in the end.
clean_syspath = sys.path

# unicode_plugin_path gets set from the vim script in plugin/unicodeit.vim
sys.path = [
    os.path.join(unicode_plugin_path,
                 'submodules',
                 'unicodeit',
                 'src')] + \
    sys.path


def UnicodeIt():
    # derived from https://stackoverflow.com/a/27936782
    import unicodeit
    buf = vim.current.buffer
    # lnum* is the line number (counting from 1)
    # col* is the column number (counting from 0)
    (lnum1, col1) = buf.mark('<')
    (lnum2, col2) = buf.mark('>')
    lines = vim.eval('getline({}, {})'.format(lnum1, lnum2))
    before = lines[0][0:col1]
    after = lines[-1][col2 + 1:]
    if len(lines) == 1:
        lines[0] = lines[0][col1:col2 + 1]
    else:
        lines[0] = lines[0][col1:]
        lines[-1] = lines[-1][:col2 + 1]

    # lines is a list of strings, potentially of length one.
    # unicodeit.replace takes a list of strings, potentially of length one and
    # returns a list of strings.

    lines = unicodeit.replace(lines)
    before = bytes(before, encoding='utf-8')
    after = bytes(after, encoding='utf-8')

    # `vim.current.buffer[2:2] = ...` inserts after line 2 (counting from 1)
    # `vim.current.buffer[2:3] = ...` replaces line 3 (counting from 1)
    if len(lines) == 1:
        vim.current.buffer[lnum1-1:lnum1] = \
            [bytes(before) + lines[0] + bytes(after)]
    elif len(lines) == 2:
        vim.current.buffer[lnum1-1:lnum1+1] = [
            before + lines[0],
            lines[1] + after]
    else:
        vim.current.buffer[lnum1-1:lnum2] = \
            [before + lines[0]] + \
            lines[1:-1] + \
            [lines[-1] + after]


UnicodeIt()
sys.path = clean_syspath
