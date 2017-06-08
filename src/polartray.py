#!/usr/bin/env python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PolarTray(Gtk.StatusIcon):
  def __init__(self):
    Gtk.StatusIcon.__init__(self)
    self.set_from_icon_name('help-about')
    self.set_has_tooltip(True)
    self.set_visible(True)
    self.connect("popup_menu", self.on_secondary_click)

    Gtk.main()

  def on_secondary_click(self, widget, button, time):
    menu = Gtk.Menu()

    menu_quit = Gtk.MenuItem("Quit")
    menu.append(menu_quit)
    menu_quit.connect("activate", Gtk.main_quit)

    menu.show_all()
    menu.popup(None, None, None, self, 3, time)

if __name__ == '__main__':
  try:
    PolarTray()
  except KeyboardInterrupt:
    print('Interrupted')
