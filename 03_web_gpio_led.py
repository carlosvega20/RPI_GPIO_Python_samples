#!/usr/bin/python
# LED Blinky code for Raspberry Pi on flask webserver
# Written in Python 2.7.3 by Carlos Vega

from flask import Flask
import RPi.GPIO as GPIO     ## Import GPIO Library
import time                 ## Import 'time' library (for 'sleep')

app = Flask(__name__)

def ledBlink(pin, delay):
    while True:
        GPIO.output(pin, GPIO.HIGH)     ## Turn on GPIO pin (HIGH)
        time.sleep(delay)               ## Wait
        GPIO.output(pin, GPIO.LOW)      ## Turn off GPIO pin (LOW)
        time.sleep(delay)               ## Wait


@app.route("/")
def hello():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    ledBlink(7, 1)
    GPIO.cleanup()
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) #Running on http://localhost:8080
