#!/usr/bin/python
# vim:ts=8:sw=4:expandtab:encoding=utf-8
'''Demo for using gtk widgets in fontforge program.
Copyright <hashao2@gmail.com> 2009

#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

Put the file in $(PREFIX)/share/fontforge/python or ~/.FontForge/python, invoke
from "Tools->Demo->Show GTK".

'''
__version__ = '0.1'


# =============== important for fontforge!!!! =================
# set proper sys.path for sub modules
def setup_syspath():
    import sys
    import os
    # setup module path for local modules of Fontforge scripts.
    # put local module in 'modules' subdirectory: ~/.FontForge/python/modules
    x = sys._getframe().f_code.co_filename
    modpath = os.path.join(os.path.dirname(x), 'modules')
    if modpath not in sys.path:
        sys.path.append(modpath)
setup_syspath()

import gdraw
import gtk
import fontforge

from kmetricwin import KMetricWin

def DemoGtk(junk, afont):
    '''Show max height and width of the selected glyphs.'''
    w = KMetricWin(junk, afont)
    
    # Start gtk loop here!
    gdraw.gtkrunner.start()

if fontforge.hasUserInterface():
    fontforge.registerMenuItem(DemoGtk, None, None, "Font", None,
            "Metrics", "Kerning Metrics");
