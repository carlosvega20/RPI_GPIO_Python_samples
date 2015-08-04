#!/usr/bin/python
# Basic blink Led code for Raspberry Pi
# Written in Python 2.7.3 by Carlos Vega

import RPi.GPIO as GPIO     ## Import GPIO Library
import time                 ## Import 'time' library (for 'sleep')

## Define default pin number to use
pin = 7;

GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering
GPIO.setup(int(pin), GPIO.OUT)  ## Set GPIO pin to OUTPUT

GPIO.output(pin, GPIO.HIGH)     ## Turn on GPIO pin LED (HIGH)
time.sleep(5)                   ## Wait 5 seconds
GPIO.output(pin, GPIO.LOW)      ## Turn off GPIO pin LED (LOW)

## Clean up at the End
GPIO.cleanup()
