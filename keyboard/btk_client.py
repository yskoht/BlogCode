# -*- coding: utf-8 -*-
import dbus
import dbus.service
import dbus.mainloop.glib
import sys
import time
from keycode import KC


class BtkClient:
    KEY_DELAY = 0.01

    def __init__(self):
        self.state = [
            0xA1,  # this is an input report
            0x01,  # Usage report = Keyboard
            [  # Bit array for Modifier keys
                0,  # Right GUI - Windows Key
                0,  # Right ALT
                0,  # Right Shift
                0,  # Right Control
                0,  # Left GUI
                0,  # Left ALT
                0,  # Left Shift
                0,  # Left Control
            ],
            0x00,  # Vendor reserved
            0x00,  # rest is space for 6 keys
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
        ]

        self.bus = dbus.SystemBus()
        self.btkservice = self.bus.get_object('org.yaptb.btkbservice', '/org/yaptb/btkbservice')
        self.iface = dbus.Interface(self.btkservice, 'org.yaptb.btkbservice')

    def send_key_state(self):
        bin_str = ""
        element = self.state[2]
        for bit in element:
            bin_str += str(bit)
        self.iface.send_keys(int(bin_str, 2), self.state[4:10])

    def send_key(self, modifiers, key):
        self.state[2] = modifiers
        self.state[4] = key.value
        self.send_key_state()

    def send(self, modifiers, key):
        self.send_key(modifiers, key)
        time.sleep(BtkClient.KEY_DELAY)


if __name__ == '__main__':
    client = BtkClient()
    for string in sys.argv[1:]:
        keycodes = KC.str2kc(string)
        for kc in keycodes:
            client.send(KC.modifiers(), kc)
