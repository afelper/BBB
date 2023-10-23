from Adafruit_BBIO.SPI import SPI
import time

# Configura los bytes para la secuencia
sequence = [0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
spi = SPI(0, 0)

#Define la velocidad de la secuencia (en segundos por paso)
secuencia_velocidad = 0.5

#Realiza la secuencia de luces
try:
    while True:
        for byte in sequence:
            spi.writebytes([byte])
            time.sleep(secuencia_velocidad)

        for byte in reversed(sequence):
            spi.writebytes([byte])
            time.sleep(secuencia_velocidad)

except KeyboardInterrupt:
    pass

spi.close()
