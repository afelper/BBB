import Adafruit_BBIO.PWM as PWM
import time

# Definir el pin y la frecuencia del PWM
pin = "P8_13"

# Inicializar el PWM
PWM.start(pin, 0)

for i in range(0,100):
    PWM.set_duty_cycle(pin, float(i))
    time.sleep(.2)

# Detener el PWM y limpiar los recursos
PWM.stop(pin)
PWM.cleanup()
