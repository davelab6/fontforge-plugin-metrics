FontForge Python Kerning Window
==========================================

This is the first project in a set of new user interfaces for FontForge, leveraging its Python scripting. 

These new UIs run from within FontForge, so that all FontForge's existing functionality is available while new features are prototyped. 

This uses PyGTK thanks to the [Font Industry](http://code.google.com/p/fontindustry/) project






This is a research project to explore ways of writing new font editor user interfaces in Python using FontForge's python plug-in system. 

By running font editor programs from within FontForge, all FontForge's existing functionality is available to users alongside the prototype. 

These plugins will use a variety of Python-based widget sets/toolkits - currently the roadmap includes. PyGTK, PyQT, Pyjamas Desktop, Pyjamas Web, PyClutter and PyMT.

*Currently the code is hosted with Git at [https://github.com/davelab6/fontforge-plugin-metrics]*


Cotola is the Venetian word for [http://en.wikipedia.org/wiki/Venetian_language "skirt"].

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
