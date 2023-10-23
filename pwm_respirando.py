import Adafruit_BBIO.PWM as PWM
import time

led_pin = "P8_13"
fading_up = True
level = 0.0

PWM.start(led_pin, level, 1000)  # 1000Hz es una frecuencia común para LED

try:
    while True:
        if level > 99:
            fading_up = False
        if level < 1:
            fading_up = True
        if fading_up:
            level = level + 1
        else:
            level = level - 1
        #print("level tiene: ",level)
        PWM.set_duty_cycle(led_pin, level)  
        time.sleep(0.01)
  
except KeyboardInterrupt:
    PWM.stop(led_pin)
    PWM.cleanup()
