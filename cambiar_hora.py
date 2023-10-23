import smbus

# Crear un objeto SMBus
i2c = smbus.SMBus(2)

# Dirección del reloj de tiempo real
direccion = 0x68

# Obtener la hora, minuto y segundo actuales en formato decimal
hora_actual = 12  # Cambia esto a la hora deseada en formato decimal (por ejemplo, 12)
minuto_actual = 10  # Cambia esto al minuto deseado en formato decimal (por ejemplo, 30)
segundo_actual = 0  # Cambia esto al segundo deseado en formato decimal (por ejemplo, 0)

# Convertir la hora, minuto y segundo en formato BCD
hora_bcd = ((hora_actual // 10) << 4) + (hora_actual % 10)
minuto_bcd = ((minuto_actual // 10) << 4) + (minuto_actual % 10)
segundo_bcd = ((segundo_actual // 10) << 4) + (segundo_actual % 10)

# Escribir la nueva hora en el RTC
i2c.write_byte_data(direccion, 0x00, segundo_bcd)  # Segundo
i2c.write_byte_data(direccion, 0x01, minuto_bcd)  # Minuto
i2c.write_byte_data(direccion, 0x02, hora_bcd)    # Hora

print("La hora ha sido cambiada a:", hora_actual, ":", minuto_actual, ":", segundo_actual)
