import smbus

# Crear un objeto SMBus
i2c = smbus.SMBus(2)

# Dirección del reloj de tiempo real
direccion = 0x68

# Leer la hora actual desde el RTC
datos_hora = i2c.read_i2c_block_data(direccion, 0x00, 7)

print(datos_hora)
# Decodificar los datos de la hora
segundo = (datos_hora[0] & 0x0F) + ((datos_hora[0] >> 4) * 10)
minuto = (datos_hora[1] & 0x0F) + ((datos_hora[1] >> 4) * 10)
hora = (datos_hora[2] & 0x0F) + ((datos_hora[2] >> 4) * 10)

# Formatear la hora en el formato de 24 horas (HH:MM:SS)
hora_formato_24hrs = f"{hora:02d}:{minuto:02d}:{segundo:02d}"

# Imprimir la hora en formato de 24 horas
print("Hora en formato de 24 horas:", hora_formato_24hrs)
