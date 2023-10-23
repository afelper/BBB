import board
import digitalio
import time

# Define el pin del pulsador
pulsador = digitalio.DigitalInOut(board.P9_12)
pulsador.direction = digitalio.Direction.INPUT

# Define el evento que queremos detectar
eventos = digitalio.Pull.BOTH

# Bucle principal
while True:
    # Verifica si el evento se ha producido
    if  pulsador.value:
        # Imprime un mensaje
        print("¡El pulsador ha sido pulsado!")
    else:
        print("El pulsador ha sido liberado!")
    time.sleep(0.5)
