import time
import smbus

# Crear un objeto SMBus
i2c = smbus.SMBus(2)

# Dirección del reloj de tiempo real
direccion = 0x68

# Leer la hora actual desde el RTC
datos_hora = i2c.read_i2c_block_data(direccion, 0x00, 3)

print(datos_hora[0:3])
# Convertir datos BCD a decimal
hora = (datos_hora[2] & 0x0F) + ((datos_hora[2] >> 4) * 10)
minuto = (datos_hora[1] & 0x0F) + ((datos_hora[1] >> 4) * 10)
segundo = (datos_hora[0] & 0x0F) + ((datos_hora[0] >> 4) * 10)

# Imprimir la hora actual en la consola
print("La hora actual es:", hora, ":", minuto, ":", segundo)

