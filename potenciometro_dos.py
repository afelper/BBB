import Adafruit_BBIO.ADC as ADC
import time

mi_pin="P9_33"

ADC.setup()

while True:
    valor = round(ADC.read(mi_pin) * 1.8, 2)
    print(f"voltaje: {valor}") 
    #print("valor: ", round(valor*1.8,2))
    time.sleep(0.5)
