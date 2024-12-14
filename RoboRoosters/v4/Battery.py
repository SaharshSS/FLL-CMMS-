from pybricks.hubs import PrimeHub

hub = PrimeHub()

print("Battery.py loaded")

def voltage():
    return hub.battery.voltage()/1000

def current():
    return hub.battery.current()/1000

def percentage(voltage):
    voltage = voltage - 7.75
    voltage = voltage * 200
    return voltage
