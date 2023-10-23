import Adafruit_BBIO.ADC as ADC
import time

mi_pin = "P9_33"

ADC.setup()

while True:
    valor = ADC.read(mi_pin)    	
    print(f"valor: {valor}")
    time.sleep(.5)