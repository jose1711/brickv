#!/usr/bin/env python

import os

def system(command):
    if os.system(command) != 0:
        exit(1)

system("pyuic4 -o ui_sound_pressure_level.py ui/sound_pressure_level.ui")
