#Sensor LDR en serie con una resistencia de 10Kohms 
#El sensor está conectado con un Ompa LF353 en modo seguidor de voltaje.

import Adafruit_BBIO.ADC as ADC
import time

sensor_pin = 'P9_39' #AIN0

ADC.setup()

print('Reading\t\tVolts')

while True:
    reading = ADC.read(sensor_pin)
    volts = reading * 1.800 # covertir a voltios
    print('%f\t%f' % (reading, volts))
    time.sleep(1)
