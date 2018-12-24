#!/bin/sh

/etc/init.d/bluetooth stop
/usr/sbin/bluetoothd --nodetach --debug -p time

