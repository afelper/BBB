#LED RGB de ánodo común, donde el LED se enciende al aplicar un 
#voltaje bajo(nivel bajo) al pin correspondiente.

import Adafruit_BBIO.PWM as PWM
import time

#Definición de pines
rojo = "P8_13"
verde = "P8_19"
azul = "P9_14"

#Inicialización de los pies PWM
PWM.start(rojo, 100) # 100% de ciclo de tragajo para apagar el rojo
PWM.start(azul, 100) # 100% de ciclo de trabajo para apagar el azul
PWM.start(verde, 100) # 100% de ciclo de trabajo para apagar el verde

# Función para realizar la transición de color suave
def fade(colorA, colorB, ignore_color):
    PWM.set_duty_cycle(ignore_color, 100) # 100% de ciclo de trabajo para apagar el color ignorado
    for i in  range(0, 100):
        PWM.set_duty_cycle(colorA, i)  #Aumentar el ciclo de trabajo de colorA
        PWM.set_duty_cycle(colorB, 100 - i) # Disminuir el ciclo de trabajo de colorB
        time.sleep(0.05)
try:
    # Bucle principal para alterar las transiciones de color
    while True:
        fade(rojo, verde, azul)
        fade(verde, azul, rojo)
        fade(azul, rojo, verde)
except KeyboardInterrupt:
    # Limpieza de los pines PWM en caso de interrupción por teclado
    PWM.stop(rojo)
    PWM.stop(verde)
    PWM.stop(azul)
    PWM.cleanup()
