#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

pin1="P9_11"
pin2="P9_12"
pin3="P9_13"
pin4="P9_14"
pin5="P9_15"
pin6="P9_16"
pin7="P9_17"
pin8="P9_18"

GPIO.setup(pin1 , GPIO.OUT)
GPIO.setup(pin2 , GPIO.OUT)
GPIO.setup(pin3 , GPIO.OUT)
GPIO.setup(pin4 , GPIO.OUT)
GPIO.setup(pin5 , GPIO.OUT)
GPIO.setup(pin6 , GPIO.OUT)
GPIO.setup(pin7 , GPIO.OUT)
GPIO.setup(pin8 , GPIO.OUT)

for i in range(0,3):
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)


    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.HIGH)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.HIGH)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.HIGH)
    GPIO.output(pin8,GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    GPIO.output(pin5,GPIO.LOW)
    GPIO.output(pin6,GPIO.LOW)
    GPIO.output(pin7,GPIO.LOW)
    GPIO.output(pin8,GPIO.HIGH)
    time.sleep(1)


