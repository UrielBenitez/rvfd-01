from machine import ADC
from time import sleep
from math import log

thermistor = ADC(26)


while True:
    lectura = thermistor.read_u16()
    print("El valor del ADC es: {}" .format(lectura))
    escalon = 3.3/65535
    tension = lectura * escalon
    print("El valor de tensión medido es: {}".format(tension))
    Rntc = 10000 /((3.3/tension)-1) #Formula para calcular la R variable del sensor
    print("El valor de resistencia del NTC es: {}".format(Rntc))
    temperatura = 3950 / (log(Rntc/10000) +(3950/298)) - 273
    print("La temperatura es:{}".format(temperatura))
    sleep(3)
