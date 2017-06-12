# polartray

This trayer is part of a project which is intended to be a full replacement for polar's sync flow software.
Unfortunatelly there is no linux/unix support available for these kind of devices and
polar doesn't plan to provide it in the near future.

## usage

This application runs as trayer. As soon as a device is connected it pops up in your traybar.
After the device initialization it will sync all files from the device to your computer and converts
the protocol buffer to json format located in ~/.local/polartray.
In this phase the icon changes to an arrow as long as the sync is in progress.

You don't need root access to run this trayer as long as you're in the users group and the
udev rule is in place.

    cp udev/99-polar.rules /etc/udev/rules.d/
    gpasswd -a <userame> users
    # be aware that you have to reboot

## tldr

### cloud devices

the idea of cloud-only devices is one of the worst inventions of human-beeing.
All these devices are developed for trash cause it works only as long as the vendor is
interested in running the backend.
As soon as the solution doesn't earn money it will be shutdown soon.
On the other hand all these devices collecting data which will be analyzed and sold to third-party instances.

Think about a future where insurences will use fitnesstracker metrics to calculate your fee.
The last 15 years of computer sience and digitalization tells us that all data will be used.

### the good

the polar loop is identified as HID USB device. It's not necessary to write a seperated kernel modules.
there is already a python library for device access.

### the bad

Metrics are stored as protocol buffers and the spec files aren't officialy available.

### the worse

The protocol buffer specs are missing in sync flow software as well as in
the smartphone apps. It looks like all metrics will decoded on server-side.
Additionaly it looks like the polar loop has implemented an internal counter
that forces a syncronization with the official backend. Otherwise it stoppes working.

### conclusion

polar electro devices are developed to lock-in all their users and sell everything they collect.
Nevertheless it is possible to use it without the cloud.
