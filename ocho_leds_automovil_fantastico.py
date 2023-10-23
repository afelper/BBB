#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

pins = ["P9_11", "P9_12", "P9_13", "P9_14", "P9_15", "P9_16", "P9_17", "P9_18"]

# Configura todos los pines como salidas
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def knight_rider_lights(iterations, speed):
    for _ in range(iterations):
        for i in range(len(pins)):
            GPIO.output(pins[i], GPIO.HIGH)  # Enciende el pin actual
            if i > 0:
                GPIO.output(pins[i - 1], GPIO.LOW)  # Apaga el pin anterior
            time.sleep(speed)
        for i in range(len(pins) - 1, -1, -1):
            GPIO.output(pins[i], GPIO.LOW)  # Apaga el pin actual
            if i < len(pins) - 1:
                GPIO.output(pins[i + 1], GPIO.HIGH)  # Enciende el siguiente pin
            time.sleep(speed)

try:
    while True:
        knight_rider_lights(3, 0.1)  # Ejecuta el efecto 3 veces con velocidad 0.1 segundos
except KeyboardInterrupt:
    pass
finally:
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)  # Apaga todos los pines al finalizar
