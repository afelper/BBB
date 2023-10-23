import Adafruit_BBIO.SPI as SPI

# Configurar la comunicación SPI
spi = SPI.SPI(0, 0)  # Bus SPI 0, dispositivo 0
spi.msh = 1000000  # Frecuencia de 1 MHz
spi.bpw = 8  # 8 bits por palabra
spi.mode = 3  # Modo 3

# Byte de dirección (0x80 para lectura) y dirección del registro (0x00 para el registro 0x00)
address_byte = 0x80 | 0x00

# Leer el registro
response = spi.xfer2([address_byte, 0x00])  # Se envía un byte de dirección 

# El ID del ADXL345 se encuentra en el byte de respuesta
sensor_id = response[1]

# Imprimir el ID del sensor
print("ID del ADXL345: 0x{:02X}".format(sensor_id))

# Cerrar la conexión SPI
spi.close()
