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

address_byte_LSB_X = 0x80 | 0x32
address_byte_MSB_X = 0x80 | 0x33
address_byte_LSB_Y = 0x80 | 0x34
address_byte_MSB_Y = 0x80 | 0x35
address_byte_LSB_Z = 0x80 | 0x36
address_byte_MSB_Z = 0x80 | 0x37


response_LSB_X = spi.xfer2([address_byte_LSB_X, 0x00])
response_MSB_X = spi.xfer2([address_byte_MSB_X, 0x00])


# Combinar los datos LSB y MSB para obtener el valor de aceleración en el eje X
acceleration_x = ((response_MSB_X[1] << 8) | response_LSB_X[1])

if (acceleration_x  >= 32768):
    acceleration_x -= 65536

response_LSB_Y = spi.xfer2([address_byte_LSB_Y, 0x00])
response_MSB_Y = spi.xfer2([address_byte_MSB_Y, 0x00])

acceleration_y = ((response_MSB_Y[1] << 8) | response_LSB_Y[1])

if (acceleration_y >= 32768):
    acceleration_y -= 65536

response_LSB_Z = spi.xfer2([address_byte_LSB_Z, 0x00])
response_MSB_Z = spi.xfer2([address_byte_MSB_Z, 0x00])

acceleration_z = ((response_MSB_Z[1] << 8) | response_LSB_Z[1])

if (acceleration_z >= 32768):
    acceleration_z -= 65536

rango_gravedad = 4 #por defecto para 2g
resolucion = 1024  # resolucion 10 bits
factor = rango_gravedad/resolucion

acceleration_x = acceleration_x * factor
acceleration_y = acceleration_y * factor
acceleration_z = acceleration_z * factor


# Imprimir el valor de aceleración en el eje y
print(f"Aceleración en el eje X: {acceleration_x: .3f}")
print(f"Aceleración en el eje Y: {acceleration_y: .3f}")
print(f"Aceleración en el eje Z: {acceleration_z: .3f}")

# Cerrar la conexión SPI
spi.close()
