import smbus
from datetime import datetime

# Crear un objeto SMBus
i2c = smbus.SMBus(2)

# Dirección del reloj de tiempo real
direccion = 0x68


# Nuevos valores para la fecha (ejemplo)
nuevo_dia_mes = 30  # Cambia esto al día deseado
nuevo_mes = 9     # Cambia esto al mes deseado
nuevo_ano = 23   # Cambia esto al año deseado

# Escribir la nueva fecha en el RTC
i2c.write_byte_data(direccion, 0x04, nuevo_dia_mes)  # Día del mes
i2c.write_byte_data(direccion, 0x05, nuevo_mes)     # Mes
i2c.write_byte_data(direccion, 0x06, nuevo_ano)     # Año

print("La fecha ha sido cambiada a:", nuevo_dia_mes, "/", nuevo_mes, "/", nuevo_ano)
