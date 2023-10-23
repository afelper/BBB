#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

pins = ["P9_11", "P9_12", "P9_13", "P9_14", "P9_15", "P9_16", "P9_17", "P9_18"]

# Configura todos los pines como salidas
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

for _ in range(3):  # Repite 3 veces
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)  # Apaga todos los pines
    time.sleep(1)

    for i, pin in enumerate(pins):
        GPIO.output(pin, GPIO.HIGH)  # Enciende el pin actual
        if i > 0:
            GPIO.output(pins[i - 1], GPIO.LOW)  # Apaga el pin anterior
        time.sleep(1)
