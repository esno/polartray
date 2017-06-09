#!/usr/bin/env python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import threading
import time

from polar import Device

class PolarTray(Gtk.StatusIcon):
  def __init__(self):
    Gtk.StatusIcon.__init__(self)
    self.set_from_icon_name('help-about')
    self.set_has_tooltip(True)
    self.set_visible(True)
    self.connect("popup_menu", self._popup)

    self.devices = {}
    self._deviceCount = 0

  def _popup(self, widget, button, time):
    menu = Gtk.Menu()

    menu_quit = Gtk.MenuItem("Quit")
    menu.append(menu_quit)
    menu_quit.connect("activate", Gtk.main_quit)

    menu.show_all()
    menu.popup(None, None, None, self, 3, time)

  def _registerDevice(self, dev):
    info = Device.get_info(dev)

    if info['serial_number'] not in self.devices:
      self.devices[info['serial_number']] = {
        'vendorId': info['vendor_id'],
        'productId': info['product_id'],
        'name': info['product_name'],
        'manufacturer': info['manufacturer']
      }
      self._deviceCount += 1

    return info

  def _scanDevices(self):
    self.scanning = True
    while self.scanning:
      devices = Device.list()

      if len(devices) > 0:
        for i, dev in enumerate(devices):
          try:
            info = self._registerDevice(dev)
            print('%s (%s)' % (info['product_name'], info['serial_number']))
          except ValueError as err:
            if 'langid' in err.message:
              print("Can't get device info. Origin Error: %s" % err)

      time.sleep(1)

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
