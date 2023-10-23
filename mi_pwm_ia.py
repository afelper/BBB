import Adafruit_BBIO.PWM as PWM
import time

def controlar_pwm(pin, frecuencia=2000, duracion=0.5):
    PWM.start(pin, 0)
    
    for i in range(0, 100):
        PWM.set_duty_cycle(pin, float(i))
        time.sleep(duracion)
    
    PWM.stop(pin)
    PWM.cleanup()

def main():
    pin_pwm = "P8_13"
    frecuencia_pwm = 2000  # Frecuencia en Hz (opcional, por defecto es 2000 Hz)
    duracion_ciclo = 0.2  # Duración de cada ciclo (opcional, por defecto es 0.2 segundos)
    
    controlar_pwm(pin_pwm, frecuencia_pwm, duracion_ciclo)

if __name__ == "__main__":
    main()
