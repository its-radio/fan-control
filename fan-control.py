#!/usr/bin/env python3
import subprocess
import time
import os

GPIO_PIN = 14
ON_TEMP = 70
OFF_TEMP = 60

def set_gpio(output):
    os.system(f'raspi-gpio set {GPIO_PIN} op')
    os.system(f'raspi-gpio set {GPIO_PIN} {"dh" if output == 0 else "dl"}')

def get_temp():
    out = subprocess.check_output(['vcgencmd', 'measure_temp'])
    temp_str = out.decode().split('=')[1].split("'")[0]
    return float(temp_str)

fan_on = False

while True:
    temp = get_temp()
    if temp >= ON_TEMP and not fan_on:
        set_gpio(0)
        fan_on = True
    elif temp <= OFF_TEMP and fan_on:
        set_gpio(1)
        fan_on = False
    time.sleep(5)
