# -*- coding: utf-8 -*-
import time
import threading
from neopixel import Adafruit_NeoPixel, Color


class LedController:
    def __init__(self,
                 num,
                 pin,
                 channel,
                 freq_hz=800000,
                 dma=10,
                 brightness=255,
                 invert=False):
        self.num = num
        self.pin = pin
        self.channel = channel
        self.freq_hz = freq_hz
        self.dma = dma
        self.brightness = brightness
        self.invert = invert

        self.strip = Adafruit_NeoPixel(self.num,
                                       self.pin,
                                       self.freq_hz,
                                       self.dma,
                                       self.invert,
                                       self.brightness,
                                       self.channel)
        time.sleep(0.01)  # 謎
        self.strip.begin()
        self.all_off()

    def off(self, i):
        self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()

    def all_off(self):
        for i in range(self.num):
            self.off(i)

    def on(self, i, color, ms=0):
        self.strip.setPixelColor(i, color)
        self.strip.show()
        if ms > 0:
            threading.Timer(ms / 1000.0, self.off, args=[i]).start()


    def end(self):
        self.all_off()
