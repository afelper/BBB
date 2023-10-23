#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

mi_led="P8_12"
mi_pulsador="P8_11"

GPIO.setup(mi_led, GPIO.OUT)
GPIO.setup(mi_pulsador, GPIO.IN)

while True:
    if GPIO.input(mi_pulsador) == False:	
        print("LED ENCENDIDO!")
        GPIO.output(mi_led,GPIO.HIGH)
    else:
        #print("LED APAGADO!")
        GPIO.output(mi_led,GPIO.LOW)	 
   
    time.sleep(0.2)
 
