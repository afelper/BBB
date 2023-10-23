#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

salida="P8_12"

GPIO.setup(salida, GPIO.OUT)

for i in range(0,5):
    GPIO.output(salida,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(salida,GPIO.LOW)
    time.sleep(1)

