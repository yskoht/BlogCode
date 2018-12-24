#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from keycode import *
from split_keyboard import SplitKeyboard
from led_controller import LedController
from neopixel import Color


LEFT_LAYOUT = [
    [KC.GRV , KC._1 , KC._2  , KC._3  , KC._4  , KC._5, KC._   ],
    [KC.TAB , KC.Q  , KC.W   , KC.E   , KC.R   , KC.T , KC._   ],
    [KC.LCTL, KC.A  , KC.S   , KC.D   , KC.F   , KC.G , KC._   ],
    [KC.LSFT, KC.Z  , KC.X   , KC.C   , KC.V   , KC.B , KC.LBRC],
    [KC.F1  , KC.ESC, KC.LALT, KC.LCMD, KC.KANA, KC.F2, KC.SPC ],
]

RIGHT_LAYOUT = [
    [KC._   , KC._6, KC._7  , KC._8  , KC._9  , KC._0  , KC.DEL ],
    [KC._   , KC.Y , KC.U   , KC.I   , KC.O   , KC.P   , KC.BSPC],
    [KC._   , KC.H , KC.J   , KC.K   , KC.L   , KC.SCLN, KC.QUOT],
    [KC.RBRC, KC.N , KC.M   , KC.COMM, KC.DOT , KC.SLSH, KC.ENT ],
    [KC.SPC , KC.F2, KC.HAEN, KC.LEFT, KC.DOWN, KC.UP  , KC.RGHT],
]

COL_PINS = [10, 22, 27, 17, 4, 3, 2]
LEFT_ROW_PINS  = [8 , 7 , 12, 16, 20]
RIGHT_ROW_PINS = [14, 15, 23, 24, 25]

LED_NUM = 32
LEFT_LED_PIN = 19
LEFT_LED_CHANNEL = 1
RIGHT_LED_PIN = 18
RIGHT_LED_CHANNEL = 0

LED_POSITION = [
    [
        [5 , 4 , 3 , 2 , 1 , 0 , None],
        [6 , 7 , 8 , 9 , 10, 11, None],
        [17, 16, 15, 14, 13, 12, None],
        [18, 19, 20, 21, 22, 23, 24  ],
        [31, 30, 29, 28, 27, 26, 25  ],
    ],
    [
        [None, 0 , 1 , 2 , 3 , 4 , 5 ],
        [None, 11, 10, 9 , 8 , 7 , 6 ],
        [None, 12, 13, 14, 15, 16, 17],
        [24  , 23, 22, 21, 20, 19, 18],
        [25  , 26, 27, 28, 29, 30, 31],
    ]
]


def get_random_christmax_color():
    v = int(255 - abs(random.normalvariate(0, 50)))
    if random.randint(0, 1) == 0:
        return Color(v, 0, 0)
    else:
        return Color(0, v, 0)


def setup_keyboard():
    left_led = LedController(LED_NUM, LEFT_LED_PIN, LEFT_LED_CHANNEL)
    right_led = LedController(LED_NUM, RIGHT_LED_PIN, RIGHT_LED_CHANNEL)

    def call_back(keys):
        if len(keys) > 0:
            print(keys)
            for k in keys:
                left_or_right = k[0]
                x = k[1]
                y = k[2]
                i = LED_POSITION[left_or_right][y][x]
                c = get_random_christmax_color()
                if left_or_right == 0:
                    left_led.on(i, c, 200)
                else:
                    right_led.on(i, c, 200)

    return SplitKeyboard(LEFT_LAYOUT,
                         RIGHT_LAYOUT,
                         COL_PINS,
                         LEFT_ROW_PINS,
                         RIGHT_ROW_PINS,
                         call_back)


if __name__ == '__main__':
    keyboard = setup_keyboard()

    try:
        print('hello')
        keyboard.start()
    except KeyboardInterrupt:
        left_led.end()
        right_led.end()
        keyboard.end()
