import Adafruit_BBIO.GPIO as GPIO
import time

mi_pin="P8_11"

GPIO.setup(mi_pin, GPIO.IN)

while True:
    GPIO.wait_for_edge(mi_pin, GPIO.FALLING)
    print("El botón ha sido presionado")
    GPIO.wait_for_edge(mi_pin, GPIO.RISING)
    print("El botón ha sido liberado")

