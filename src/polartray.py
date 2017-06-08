#!/usr/bin/env python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import threading
import time

class PolarTray(Gtk.StatusIcon):
  def __init__(self):
    Gtk.StatusIcon.__init__(self)
    self.set_from_icon_name('help-about')
    self.set_has_tooltip(True)
    self.set_visible(True)
    self.connect("popup_menu", self._popup)

  def _popup(self, widget, button, time):
    menu = Gtk.Menu()

    menu_quit = Gtk.MenuItem("Quit")
    menu.append(menu_quit)
    menu_quit.connect("activate", Gtk.main_quit)

    menu.show_all()
    menu.popup(None, None, None, self, 3, time)

  def _scanDevices(self):
    self.scanning = True
    while self.scanning:
      print('scanning')
      time.sleep(0.2)

  def run(self):
    self.threadDeviceScan = threading.Thread(target = self._scanDevices)
    self.threadDeviceScan.daemon = True
    self.threadDeviceScan.start()

    Gtk.main()

if __name__ == '__main__':
  try:
    PolarTray().run()
  except KeyboardInterrupt:
    print('Interrupted')
