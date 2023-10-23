#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

pins = ["P9_11", "P9_12", "P9_13", "P9_14", "P9_15", "P9_16", "P9_17", "P9_18"]

# Configura todos los pines como salidas
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def police_lights(duration):
    for _ in range(duration):
        for i in range(len(pins)):
            if i % 2 == 0:
                GPIO.output(pins[i], GPIO.HIGH)  # Enciende los pines pares
            else:
                GPIO.output(pins[i], GPIO.LOW)   # Apaga los pines impares
        time.sleep(0.5)
        for i in range(len(pins)):
            if i % 2 == 0:
                GPIO.output(pins[i], GPIO.LOW)   # Apaga los pines pares
            else:
                GPIO.output(pins[i], GPIO.HIGH)  # Enciende los pines impares
        time.sleep(0.5)

try:
    while True:
        police_lights(5)  # Ejecuta el patrón durante 5 segundos
except KeyboardInterrupt:
    pass
finally:
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)  # Apaga todos los pines al finalizar
