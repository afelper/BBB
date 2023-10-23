import Adafruit_BBIO.GPIO as GPIO
import time

mi_pin="P9_12"

GPIO.setup(mi_pin, GPIO.IN)

while True:
    if not  GPIO.input(mi_pin):
        print("El botón ha sido presionado!")
        while not GPIO.input(mi_pin):
            time.sleep(0.01)
        print("El botón ha sido liberado!")
    time.sleep(0.01)
