import smbus
import time

# Dirección del RTC DS3231 en el bus I2C
direccion = 0x68

# Crear un objeto SMBus
i2c = smbus.SMBus(2)  # El número 1 indica el bus I2C en Raspberry Pi

# Configurar la alarma 1 para que se active cuando la hora y los minutos coincidan
# Aquí configuramos la alarma para que suene a las 12:30 PM (formato de 24 horas)
# Puedes ajustar los valores según tus necesidades
hora_alarma = 0x15  # 12 en formato BCD
minuto_alarma = 0x58  # 30 en formato BCD

# Habilitar la alarma 1
i2c.write_byte_data(direccion, 0x0E, 0b00000000)  # Deshabilitar la alarma 1
i2c.write_byte_data(direccion, 0x08, minuto_alarma)  # Configurar los minutos
i2c.write_byte_data(direccion, 0x09, hora_alarma)    # Configurar la hora
i2c.write_byte_data(direccion, 0x0A, 0b10000000)  # Habilitar la alarma 1

# Leer la hora actual
i2c.write_byte(direccion, 0x00)
datos_hora = i2c.read_i2c_block_data(direccion, 0x00, 7)

# Decodificar los datos de la hora
segundo = (datos_hora[0] & 0x0F) + ((datos_hora[0] >> 4) * 10)
minuto = (datos_hora[1] & 0x0F) + ((datos_hora[1] >> 4) * 10)
hora = (datos_hora[2] & 0x0F) + ((datos_hora[2] >> 4) * 10)

print("Hora actual:", hora, ":", minuto, ":", segundo)

# Esperar a que se active la alarma (puedes realizar otras tareas aquí)
while True:
    # Leer el registro de estado de las alarmas para verificar si la Alarma 1 se ha activado
    estado_alarmas = i2c.read_byte_data(direccion, 0x0F)
    if estado_alarmas & 0b00000001:
        print("¡Alarma 1 activada!")
        break
    time.sleep(1)  # Esperar un segundo antes de verificar nuevamente
