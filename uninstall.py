#!/usr/bin/env python3
# coding: utf-8
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import platform
import glob
import os
import shutil
import sys

os_type = platform.system()

if os_type == 'Linux':
    path_list = ['/usr/share/man/man1/persepolis.1.gz',
                 '/usr/share/pixmaps/persepolis.svg',
                 '/usr/share/pixmaps/persepolis-tray.svg',
                 '/usr/share/applications/com.github.persepolisdm.persepolis.desktop',
                 '/usr/share/metainfo/com.github.persepolisdm.persepolis.appdata.xml',
                 '/usr/bin/persepolis']

    # finding persepolis directories in /usr/lib/python3.6/site-packages/
    pattern = os.path.join('/usr/lib/python3.6/site-packages/', 'persepolis*')
    for folder in glob.glob(pattern):
        path_list.append(folder)

elif os_type == 'FreeBSD' or os_type == 'OpenBSD':
    path_list = ['/usr/local/share/man/man1/persepolis.1.gz',
                 '/usr/local/share/pixmaps/persepolis.svg',
                 '/usr/local/share/pixmaps/persepolis-tray.svg',
                 '/usr/local/share/applications/com.github.persepolisdm.persepolis.desktop',
                 '/usr/local/share/metainfo/com.github.persepolisdm.persepolis.appdata.xml',
                 '/usr/local/bin/persepolis']

    # finding persepolis directories in /usr/lib/python3.6/site-packages/
    pattern = os.path.join('/usr/local/lib/python3.6/site-packages/', 'persepolis*')
    for folder in glob.glob(pattern):
        path_list.append(folder)

    # finding persepolis directories in /usr/lib/python3.6/site-packages/
    pattern = os.path.join('/usr/local/lib/python3.5/site-packages/', 'persepolis*')
    for folder in glob.glob(pattern):
        path_list.append(folder)

else:
    print('This script is for Linux and BSD')
    sys.exit(1)

uid = os.getuid()
if uid != 0:
    print('run this script as root.')
    sys.exit(1)


for path in path_list:
    if os.path.exists(path):
        if os.path.isfile(path):  # if path is for file
            os.remove(path)  # removing file
        else:
            shutil.rmtree(path)  # removing folder
        print(str(path) + ' is removed!')

print('uninstallation is complete!')
