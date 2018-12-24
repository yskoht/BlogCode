# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from btk_client import BtkClient
from keycode import KC


class SplitKeyboard:
    def __init__(self,
                 left_layout,
                 right_layout,
                 col_pins,
                 left_row_pins,
                 right_row_pins,
                 call_back=None):
        self.left_layout = left_layout
        self.right_layout = right_layout
        self.col_pins = col_pins
        self.left_row_pins = left_row_pins
        self.right_row_pins = right_row_pins
        self.call_back = call_back

        self.keys = []
        self.btk_client = BtkClient()

        GPIO.setmode(GPIO.BCM)
        for p in self.col_pins:
            GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)
        for p in self.left_row_pins:
            GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for p in self.right_row_pins:
            GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def send(self):
        ks = [_[3] for _ in self.keys]
        self.btk_client.send(KC.modifiers(ks), KC.key(ks))

        if self.call_back is not None:
            self.call_back(self.keys)

    def start(self):
        while True:
            self.keys = []
            for x, col_pin in enumerate(self.col_pins):
                GPIO.output(col_pin, 1)
                for y, (left_row_pin, right_row_pin) in enumerate(zip(self.left_row_pins, self.right_row_pins)):
                    if GPIO.input(left_row_pin) == 1:
                        self.keys.append((0, x, y, self.left_layout[y][x]))
                    if GPIO.input(right_row_pin) == 1:
                        self.keys.append((1, x, y, self.right_layout[y][x]))
                GPIO.output(col_pin, 0)
            self.send()

    @staticmethod
    def end():
        GPIO.cleanup()
