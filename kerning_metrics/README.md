FontForge Plugins
===================

This is a project to write new font editor user interfaces, using PyGTK from within FontForge, so that all FontForge's existing functionality is available while new features are prototyped. 

INSTALLATION
==============
```sh
wget http://fontindustry.googlecode.com/files/fontforge-pygtk-0.1.tar.bz2;
bunzip2 fontforge-pygtk-0.1.tar.bz2;
tar xfv fontforge-pygtk-0.1.tar;
sudo cp -rpa fontforge-pygtk-0.1/modules/gdraw /usr/lib/python2.6/;
make ;
```
Then run FontForge in the usual way, and run the plugins from the Tools menu.
