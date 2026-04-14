#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script
Do your stuff here, similar to the loop() function on Arduino
"""

from be_upy_blink import flash_led
from machine import Pin
try:
    from os import uname
except ImportError:
    # u-packages might be deprecated in future
    from uos import uname
from time import sleep


def loop():
    os_info = uname()

    # set pin as output
    if 'pyboard' in os_info:
        led_pin = Pin(1, Pin.OUT)
    elif 'esp8266' in os_info:
        led_pin = Pin(2, Pin.OUT)
    elif 'esp32' in os_info:
        led_pin = Pin(2, Pin.OUT)
    elif 'rp2' in os_info:
        # RP2 has the LED on pin 25, Pico W on a custom pin routed to "LED"
        led_pin = Pin("LED", Pin.OUT)
    else:
        raise Exception("Unknown board, manually extend main.py")

    # turn it off
    led_pin.value(0)

    # loop forever
    while True:
        # flash LED 3 times, being each 1 second on and 3 seconds off
        # then sleep for 3 seconds and repeat
        flash_led(pin=led_pin, amount=3, on_time=1, off_time=2)
        sleep(3)


# MicroPython calls every function inside this file
loop()
