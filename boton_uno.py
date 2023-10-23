import Adafruit_BBIO.GPIO as GPIO
import time

pin="P9_12"

GPIO.setup(pin, GPIO.IN)

while True:
    if not  GPIO.input(pin):
        print("El botón ha sido presionado!")
    time.sleep(0.1)
