#!/usr/bin/env python
'''UI Manager

The GtkUIManager object allows the easy creation of menus
from an array of actions and a description of the menu hierarchy.
'''
# pygtk version: Maik Hertha <maik.hertha@berlin.de>

import gobject
import gtk
import fontforge
import gdraw

def activate_action(action):
    print 'Action "%s" activated' % action.get_name()

def activate_radio_action(action, current):
    print 'Radio action "%s" selected'% current.get_name()

import sys
import os
modpath = sys._getframe().f_code.co_filename
modpath = os.path.dirname(modpath)


class KMetricWin:
    
    def g(self, id):
        return self.b.get_object(id)
        
    def __init__(self, junk, afont):
        self.junk = junk
        self.afont = afont

        self.b = gtk.Builder()
        self.b.add_from_file(os.path.join(modpath, 'ui.glade'))
        self.w = self.g('mainwin')
        
        self.ph = self.g('prog_header')
        self.ps = self.g('prog_subhead')
        self.pl = self.g('prog_line')
        self.pb = self.g('progress')
        
        # Set up DND
        #self.dndsetup()
        
        # Set up chooser
        #self.chooseboxsetup()
        
        self.b.connect_signals(self)
        self.w.show_all()
        
    def dndsetup(self):
        self.treeview = self.g('mainview')
        # Model: Stock icon (shown), label (marked up, shown), path (not shown)
        self.treeview.set_model(gtk.ListStore(str, str, str))
        x = gtk.CellRendererText()
        x.markup = True
        self.treeview.append_column(gtk.TreeViewColumn('Icon', gtk.CellRendererPixbuf(), stock_id=0))        
        self.treeview.append_column(gtk.TreeViewColumn('URL', x, markup=1))
                
        self.treeview.enable_model_drag_dest([
                                                    ('MY_TREE_MODEL_ROW', gtk.TARGET_SAME_WIDGET, 0),
                                                    ('text/plain', 0, 1),
                                                    ('TEXT', 0, 2),
                                                    ('STRING', 0, 3),
                                             ],
                                             gtk.gdk.ACTION_DEFAULT)
        
        self.treeview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)

        self.treeview.connect("drag_data_received", self.drag_data_received_data)
        
    def chooseboxsetup(self):
        self.ch = self.g('choosebox')
        # Model: Label (shown), extension (not shown)
        model = gtk.ListStore(str, str)
        self.ch.set_model(model)
        self.cell = gtk.CellRendererText()
        self.ch.pack_start(self.cell, True)
        self.ch.add_attribute(self.cell, 'text', 0)
        fx = self.font_exts.items()
        fx.sort()
        # TODO: Could be prettier.
        i = 0
        for k, v in fx:
            model.append([("Output %s (%s)" % (v, k)), k])
            if (k == 'ttf'):
                j = i
            i += 1
        self.ch.set_active(j)
        
    def quit(self, widget):
        #self.destroy()
        gdraw.gtkrunner.stop()
    
    def del_button_clicked_cb(self, widget):
        sel = self.treeview.get_selection()
        selection = self.treeview.get_selection()
        model, selected = selection.get_selected_rows()
        iters = [model.get_iter(path) for path in selected]
        for iter in iters:
            model.remove(iter)
            
    def add_button_clicked_cb(self, widget):
        diag = gtk.FileChooserDialog('Add a font file', None, gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        diag.set_default_response(gtk.RESPONSE_OK)        
        response = diag.run()
        if response == gtk.RESPONSE_OK:
            self.addpath(diag.get_filename())
        diag.destroy()
    
    def exec_button_clicked_cb(self, widget):
        self.pw = self.b.get_object('progresswin')
        self.w.hide()
        self.pw.show_all()
        self.makescript()
    
    def closebutton_clicked_cb(self, widget):
        self.pw.hide()
        self.w.show()
        
    def clear_button_clicked_cb(self, widget):
        self.treeview.get_model().clear()
        
    def about_button_clicked_cb(self, widget):
        self.b.get_object('adiag').show()
        
    def adiag_hide(self, widget, dunno):
        self.b.get_object('adiag').hide()
    
    def addpath(self, path):
        model = self.treeview.get_model()
        fname = path.split(os.sep)[-1]
        fext = fname.split('.')[-1]        
        if not os.path.isfile(path):
            print data, "couldn't be turned into a path."
            return
        
        if not str(fext).lower() in self.font_exts:
            print fname, "didn't match a font extension."
            return
        
        label =  "%s <span color='gray'>%s</span>" % (path.split(os.sep)[-1], self.font_exts[str(fext).lower()])
        model.append([gtk.STOCK_FILE, label, path])

        
    def drag_data_received_data(self, treeview, context, x, y, selection,
                                info, etime):
        model = treeview.get_model()
        data = str(selection.data)
        files = data.splitlines()
        for file in files:
            path = str(urllib.unquote(file)).replace('file://', '')
            self.addpath(path)
        return
    
