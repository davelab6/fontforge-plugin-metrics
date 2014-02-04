FontForge Python Kerning Window
==========================================

This is the first plugin in the "Cortola" project: to create new user interfaces for FontForge, leveraging its Python scripting. 

These new UIs run from within FontForge, so that all FontForge's existing functionality is available while new features are prototyped. 

This uses PyGTK thanks to the [Font Industry](http://code.google.com/p/fontindustry/) project. Other plugins could choose from a variety of Python-based widget sets/toolkits, such as PyQT, PyClutter and PyMT.

_Cotola is the Venetian word for ['skirt'](http://en.wikipedia.org/wiki/Venetian_language)_

INSTALLATION
==============
```sh
bunzip2 fontforge-pygtk-0.1.tar.bz2;
tar xfv fontforge-pygtk-0.1.tar;
sudo cp -rpa fontforge-pygtk-0.1/modules/gdraw /usr/lib/python2.6/;
cp -aux modules ~/.FontForge/python;
cp -aux kmetrics.py ~/.FontForge/python;
fontforge;
```
You will now find the new Metrics Window in the Tools menu.
