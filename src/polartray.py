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
    self.set_visible(False)
    self.set_from_icon_name('help-about')
    self.set_has_tooltip(True)
    self.connect("popup_menu", self._popup)

    self.deviceCount = 0
    self.devices = {}

  def _popup(self, widget, button, time):
    menu = Gtk.Menu()

    for k, v in self.devices.iteritems():
      menuDevice = Gtk.MenuItem('%s (%s)' % (v['name'], k))
      menu.append(menuDevice)

    menuQuit = Gtk.MenuItem('Quit')
    menuQuit.connect("activate", Gtk.main_quit)
    menu.append(menuQuit)

    menu.show_all()
    menu.popup(None, None, None, self, 3, time)

  def _registerDevice(self, dev):
    info = Device.get_info(dev)

    if info['serial_number'] not in self.devices:
      print('register device %s (%s)' % (info['product_name'], info['serial_number']))
      self.devices[info['serial_number']] = {
        'vendorId': info['vendor_id'],
        'productId': info['product_id'],
        'name': info['product_name'],
        'manufacturer': info['manufacturer'],
        'device': dev
      }
      self.deviceCount += 1

    return info

  def _scanDevices(self):
    self.scanning = True
    while self.scanning:
      devices = Device.list()
      scannedDevices = {}

      if len(devices) > 0:
        for i, dev in enumerate(devices):
          try:
            info = self._registerDevice(dev)
            scannedDevices[info['serial_number']] = {
              'vendorId': info['vendor_id'],
              'productId': info['product_id'],
              'name': info['product_name'],
              'manufacturer': info['manufacturer'],
              'device': dev
            }
          except ValueError as err:
            if 'langid' in err.message:
              print("Can't get device info. Origin Error: %s" % err)

      self._unregisterDevices({ k: self.devices[k] for k in set(self.devices) - set(scannedDevices) })

      if self.deviceCount > 0:
        self.set_visible(True)
      else:
        self.set_visible(False)

      time.sleep(1)

  def _unregisterDevices(self, devices):
    for k, v in devices.iteritems():
      print('unregister device %s (%s)' % (v['name'], k))
      self.devices.pop(k, None)
      self.deviceCount -= 1

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
