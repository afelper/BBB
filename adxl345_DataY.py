import Adafruit_BBIO.SPI as SPI

# Configurar la comunicación SPI
spi = SPI.SPI(0, 0)  # Bus SPI 0, dispositivo 0
spi.msh = 1000000  # Frecuencia de 1 MHz
spi.bpw = 8  # 8 bits por palabra
spi.mode = 3  # Modo 3

# Configurar el bit de medición en la dirección 0x2D (Registro POWER_CTL) con 0x08 para activar la medición
address_byte = 0x2D
measurement_value = 0x08
spi.xfer2([address_byte, measurement_value])

# Leer los datos de aceleración en el eje X desde las direcciones 0x32 y 0x33
# El byte menos significativo (LSB) está en 0x32 y el byte más significativo (MSB) en 0x33
address_byte_LSB = 0x80 | 0x34
address_byte_MSB = 0x80 | 0x35

# Leer el LSB y el MSB de la aceleración en el eje X (dos bytes)
#el segundo 0x00 es byte ficticio que rellena la longitud de la transferencia a 2 bytes de longutd.
#se escoge el segundo byte es lo que se leyó miemtras se escribía el segundo byte..
response_LSB = spi.xfer2([address_byte_LSB, 0x00])
response_MSB = spi.xfer2([address_byte_MSB, 0x00])

print(response_LSB)
print(response_MSB)
# Combinar los datos LSB y MSB para obtener el valor de aceleración en el eje X
acceleration_y = ((response_MSB[1] << 8) | response_LSB[1])

#complemento a dos
#if (acceleration_y & 0x8000) != 0:
#    acceleration_y = -(65536 - acceleration_y)

#if (acceleration_y & (1<<16-1)):
#   acceleration_y = acceleration_y - (1 << 16)

if (acceleration_y  >= 32768):
    acceleration_y -= 65536

rango_gravedad = 4
resolucion = 1024
factor = rango_gravedad/resolucion

acceleration_y = acceleration_y * factor

# Imprimir el valor de aceleración en el eje y
print(f"Aceleración en el eje Y: {acceleration_y: .3f}")

# Cerrar la conexión SPI
spi.close()
