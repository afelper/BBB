from Adafruit_BBIO.SPI import SPI
import time

data_to_send = [0x0f,0xf0,0x00]

spi = SPI(0,0)
for byte in data_to_send: 
    spi.writebytes([byte])
    time.sleep(1)
spi.close()

