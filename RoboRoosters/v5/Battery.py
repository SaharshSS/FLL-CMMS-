from pybricks.hubs import PrimeHub
import Math

hub = PrimeHub()

print("Battery.py loaded")

def voltage():
    return hub.battery.voltage()/1000

def current():
    return hub.battery.current()/1000

def percentage(voltage):
    return (round(Math.constrain(Math.reMap(voltage, 6.2, 8.3, 0, 100), 0, 100)*100)/100)
