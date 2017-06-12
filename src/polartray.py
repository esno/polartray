#!/usr/bin/env python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

import os
import threading
import time

from google.protobuf.json_format import MessageToJson
from protobuf import act_dailygoal_pb2
from protobuf import act_samples_pb2
from protobuf import dailysummary_pb2
from protobuf import device_pb2
from protobuf import identification_pb2
from protobuf import recovery_times_pb2
from protobuf import syncinfo_pb2
from protobuf import user_database_pb2
from protobuf import user_devset_pb2
from protobuf import user_id_pb2
from protobuf import user_physdata_pb2
from protobuf import user_prefs_pb2

from polar import Device

class PolarTray(Gtk.StatusIcon):
  FILE_MAPPINGS = {
    'DGOAL.BPB'   : act_dailygoal_pb2   .PbDailyActivityGoal,
    'ASAMPL0.BPB' : act_samples_pb2     .PbActivitySamples,
    'DSUM.BPB'    : dailysummary_pb2    .PbDailySummary,
    'DEVICE.BPB'  : device_pb2          .PbDeviceInfo,
    'ID.BPB'      : identification_pb2  .PbIdentifier,
    'RECOVS.BPB'  : recovery_times_pb2  .PbRecoveryTimes,
    'SYNCINFO.BPB': syncinfo_pb2        .PbSyncInfo,
    'UDB.BPB'     : user_database_pb2   .PbUserDb,
    'UDEVSET.BPB' : user_devset_pb2     .PbUserDeviceSettings,
    'USERID.BPB'  : user_id_pb2         .PbUserIdentifier,
    'PHYSDATA.BPB': user_physdata_pb2   .PbUserPhysData,
    'PREFS.BPB'   : user_prefs_pb2      .PbGeneralPreferences
  }

  def __init__(self):
    Gtk.StatusIcon.__init__(self)
    self.set_visible(False)
    self.set_from_icon_name('preferences-system-sharing')
    self.set_has_tooltip(True)
    self.connect("popup_menu", self._popup)

    self.deviceCount = 0
    self.syncCount = 0
    self.devices = {}

    if not os.path.isdir('%s/.local/polartray' % (os.environ['HOME'])):
      os.makedirs('%s/.local/polartray' % (os.environ['HOME']))

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

    devMap = device.walk(device.SEP)
    print('syncing device %s (%s)' % (
      self.devices[serial]['name'],
      serial
    ))
    for directory in devMap.keys():
      osDirectory = directory.replace(device.SEP, os.sep)
      d = devMap[directory]
      files = [e for e in d.entries if not e.name.endswith(os.sep)]
      for file in files:
        parserFailed = False
        if '.BPB' in file.name:
          data = device.read_file('%s%s' % (directory, file.name))

          dataFileName = '%s%s%s' % (
            serial,
            directory.replace(os.sep, '-').lower(),
            os.path.splitext(file.name)[0].lower()
          )

          if file.name in self.FILE_MAPPINGS.keys():
            parser = self.FILE_MAPPINGS[file.name]()

            if file.name == 'SAMPLES.GZB':
              data = zlib.decompress(data)

            f = '%s/.local/polartray/%s.json' % (os.environ['HOME'], dataFileName)
            try:
              parser.ParseFromString(bytes(bytearray(data)))
              with open(f, 'w') as fh:
                fh.write(MessageToJson(parser))
            except Exception as err:
              parserFailed = True
              print('failed to decode %s' % (dataFileName))
              print(err)

          if file.name not in self.FILE_MAPPINGS.keys() or parserFailed == True:
            f = '%s/.local/polartray/%s%s' % (
              os.environ['HOME'],
              dataFileName,
              os.path.splitext(file.name)[1].lower()
            )
            with open(f, 'wb') as fh:
              fh.write(bytearray(data))

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
