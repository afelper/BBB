#LM35 conectado a 5v del P9->5VX(alimentación externa)
#10mV = 1°C| max 150°C  

import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

while True:
    mV = ADC.read("P9_40") * 1800 #convertir a miliVoltios 
    #print("mV: ", mV)
    celsius = mV / 10 # miliVoltios a celsius
    fahrenheit = (celsius * 9/5) + 32 # Celsius a Fahrenheit
    print("Celsius: ", round(celsius, 1))
    print("Fahrenheit: ", round(fahrenheit, 1))
    time.sleep(1)
