#!/usr/bin/env python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

import threading
import time

from polar import Device

class PolarTray(Gtk.StatusIcon):
  def __init__(self):
    Gtk.StatusIcon.__init__(self)
    self.set_visible(False)
    self.set_from_icon_name('preferences-system-sharing')
    self.set_has_tooltip(True)
    self.connect("popup_menu", self._popup)

    self.deviceCount = 0
    self.syncCount = 0
    self.devices = {}

  def _changeIcon(self, sync):
    if sync == True:
      self.syncCount += 1
    else:
      self.syncCount -= 1

    if self.syncCount > 0:
      self.set_from_icon_name('stock_save')
    else:
      self.set_from_icon_name('preferences-system-sharing')

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

      self.devices[info['serial_number']]['thread'] = threading.Thread(
        target = self._syncDevice,
        args = [info['serial_number']]
      )
      self.devices[info['serial_number']]['thread'].start()

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
      GLib.idle_add(self._toggleTray)
      time.sleep(1)

  def _syncDevice(self, serial):
    print('connecting device %s (%s)' % (
      self.devices[serial]['name'],
      serial
    ))
    device = Device(self.devices[serial]['device'])
    device.open()
    syncing = True

    GLib.idle_add(self._changeIcon, True)

    while syncing:
      syncing = False
      time.sleep(1)

    GLib.idle_add(self._changeIcon, False)

    print('disconnecting device %s (%s)' % (
      self.devices[serial]['name'],
      serial
    ))
    device.close()

  def _toggleTray(self):
    if self.deviceCount > 0:
      self.set_visible(True)
    else:
      self.set_visible(False)

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
