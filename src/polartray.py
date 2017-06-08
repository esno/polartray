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

    Gtk.main()

if __name__ == '__main__':
  try:
    PolarTray()
  except KeyboardInterrupt:
    print('Interrupted')
