from pybricks.parameters import Icon
from pybricks.hubs import PrimeHub

hub = PrimeHub()

def char(char):
    hub.display.char(str(char))

def number(displayVal, displayOn = False): #Switch between fonts
    if displayOn == True:
        hub.display.off()
        displayOn = False
    else:
        displayOn = True
        if isinstance(displayVal, int):
            if displayVal < 10 and displayVal >= 0:
                char(displayVal)
            else:
                hub.display.number(int(displayVal))
        else:
            char(displayVal)
    return displayOn

print("Display.py loaded")
