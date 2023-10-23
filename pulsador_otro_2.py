import board
import digitalio
import time

# Configura el pin GPIO al que está conectado el pulsador
pulsador_pin = digitalio.DigitalInOut(board.P9_12)
pulsador_pin.direction = digitalio.Direction.INPUT
pulsador_pin.pull = digitalio.Pull.DOWN  # Configura la resistencia pull-down


while True:
    if not pulsador_pin.value:  # Si el pulsador está presionado
        print("Pulsador presionado")
        while not pulsador_pin.value:
            time.sleep(0.5)
        print("Pulsador liberado")
    time.sleep(0.5)


