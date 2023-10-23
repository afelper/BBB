import smbus
from datetime import datetime

# Crear un objeto SMBus
i2c = smbus.SMBus(2)

# Dirección del reloj de tiempo real
direccion = 0x68

# Leer la hora actual desde el RTC
datos_hora = i2c.read_i2c_block_data(direccion, 0x00, 7)

# Decodificar los datos de la hora
dia_semana = datos_hora[3]
dia_mes = datos_hora[4]
mes = datos_hora[5]
ano = datos_hora[6] + 2000  # Suma 2000 para obtener el año completo (20xx)

#print(segundo)
#print(minuto)
#print(hora)
#print(dia_semana)
#print(dia_mes)
#print(mes)
#print(ano)

# Crear un objeto datetime con los datos
fecha_hora = datetime(ano, mes, dia_mes)

# Obtener el nombre del día de la semana
nombre_dia_semana = fecha_hora.strftime("%A")

# Imprimir los resultados
print("Día de la semana:", nombre_dia_semana)
print("Fecha:", fecha_hora.strftime("%d/%m/%Y"))
