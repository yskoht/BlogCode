# -*- coding: utf-8 -*-
from enum import Enum
from collections import OrderedDict

class KC(Enum):
    _ = 0

    A    = 4
    B    = 5
    C    = 6
    D    = 7
    E    = 8
    F    = 9
    G    = 10
    H    = 11
    I    = 12
    J    = 13
    K    = 14
    L    = 15
    M    = 16
    N    = 17
    O    = 18
    P    = 19
    Q    = 20
    R    = 21
    S    = 22
    T    = 23
    U    = 24
    V    = 25
    W    = 26
    X    = 27
    Y    = 28
    Z    = 29

    _1   = 30
    _2   = 31
    _3   = 32
    _4   = 33
    _5   = 34
    _6   = 35
    _7   = 36
    _8   = 37
    _9   = 38
    _0   = 39

    ENT  = 40
    ESC  = 41
    BSPC = 42
    TAB  = 43
    SPC  = 44
    MINS = 45
    EQL  = 46
    LBRC = 47
    RBRC = 48
    BSLS = 50
    SCLN = 51
    QUOT = 52
    GRV  = 53
    COMM = 54
    DOT  = 55
    SLSH = 56
    CAPS = 57

    F1   = 58
    F2   = 59
    F3   = 60
    F4   = 61
    F5   = 62
    F6   = 63
    F7   = 64
    F8   = 65
    F9   = 66
    F10  = 67
    F11  = 68
    F12  = 69

    PSCR = 70
    SLCK = 71
    PAUS = 72
    INS  = 73
    HOME = 74
    PGUP = 75
    DEL  = 76
    END  = 77
    PGDN = 78
    RGHT = 79
    LEFT = 80
    DOWN = 81
    UP   = 82
    NLCK = 83
    PSLS = 84
    PAST = 85
    PMNS = 86
    PPLS = 87
    PENT = 88

    KP1  = 89
    KP2  = 90
    KP3  = 91
    KP4  = 92
    KP5  = 93
    KP6  = 94
    KP7  = 95
    KP8  = 96
    KP9  = 97
    KP0  = 98

    KPDOT = 99
    NUBS  = 100
    APP   = 101
    POWER = 102
    PEQL  = 103

    F13  = 104
    F14  = 105
    F15  = 106
    F16  = 107
    F17  = 108
    F18  = 109
    F19  = 110
    F20  = 111
    F21  = 112
    F22  = 113
    F23  = 114
    F24  = 115

    EXEC = 116
    HELP = 117
    MENU = 118
    SLCT = 119
    AGIN = 121
    UNDO = 122
    CUT  = 123
    COPY = 124
    PSTE = 125

    PCMM = 133

    RO   = 135
    KANA = 136
    JYEN = 137
    HENK = 138
    MHEN = 139
    INT6 = 140

    HAEN  = 144
    HANJ  = 145
    LANG3 = 146
    LANG4 = 147
    LANG5 = 148

    LCTL = 224
    LSFT = 225
    LALT = 226
    LCMD = 227
    RCTL = 228
    RSFT = 229
    RALT = 230
    RCMD = 231

    # PLAYPAUSE = 232
    # STOPCD = 233
    # PREVIOUSSONG = 234
    # NEXTSONG = 235
    # EJECTCD = 236
    # VOLUMEUP = 237
    # VOLUMEDOWN = 238
    # MUTE = 239

    WHOM = 240
    WBAK = 241
    WFWD = 242
    WSTP = 243
    WREF = 244

    # SCROLLUP = 245
    # SCROLLDOWN = 246
    # EDIT = 247
    # SLEEP = 248
    # COFFEE = 249
    # REFRESH = 250
    # CALC = 251

    @staticmethod
    def modifiers(_keycodes=None):
        keycodes = [] if _keycodes is None else _keycodes
        mods = OrderedDict([
            (KC.RCMD, 0),
            (KC.RALT, 0),
            (KC.RSFT, 0),
            (KC.RCTL, 0),
            (KC.LCMD, 0),
            (KC.LALT, 0),
            (KC.LSFT, 0),
            (KC.LCTL, 0),
        ])
        for kc in keycodes:
            if kc in mods:
                mods[kc] = 1
        return [_ for _ in mods.values()]

    @staticmethod
    def key(_keycodes=None):
        keycodes = [] if _keycodes is None else _keycodes
        mods = [
            KC.RCMD,
            KC.RALT,
            KC.RSFT,
            KC.RCTL,
            KC.LCMD,
            KC.LALT,
            KC.LSFT,
            KC.LCTL,
        ]
        for kc in keycodes:
            if kc not in mods:
                return kc
        return KC._

    @staticmethod
    def str2kc(string):
        str2kc_dict = {
            'A': KC.A,
            'B': KC.B,
            'C': KC.C,
            'D': KC.D,
            'E': KC.E,
            'F': KC.F,
            'G': KC.G,
            'H': KC.H,
            'I': KC.I,
            'J': KC.J,
            'K': KC.K,
            'L': KC.L,
            'M': KC.M,
            'N': KC.N,
            'O': KC.O,
            'P': KC.P,
            'Q': KC.Q,
            'R': KC.R,
            'S': KC.S,
            'T': KC.T,
            'U': KC.U,
            'V': KC.V,
            'W': KC.W,
            'X': KC.X,
            'Y': KC.Y,
            'Z': KC.Z,
            '1': KC._1,
            '2': KC._2,
            '3': KC._3,
            '4': KC._4,
            '5': KC._5,
            '6': KC._6,
            '7': KC._7,
            '8': KC._8,
            '9': KC._9,
            '0': KC._0,
            ' ': KC.SPC,
        }
        return [str2kc_dict.get(_.upper(), KC.DOT) for _ in string]

