import board
import digitalio
import time

# Configurar el pin GPIO al que está conectado el LED
pin_led = digitalio.DigitalInOut(board.P8_12)  # Reemplaza 'X' con el número de pin adecuado
pin_led.direction = digitalio.Direction.OUTPUT


while True:
    # Encender el LED
    pin_led.value = True
    print("LED encendido")
    time.sleep(1)  # Esperar 1 segundo

    # Apagar el LED
    pin_led.value = False
    print("LED apagado")
    time.sleep(1)  # Esperar 1 segundo



