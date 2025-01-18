from pybricks.parameters import Icon
from pybricks.hubs import PrimeHub

hub = PrimeHub()
hub.display.icon(Icon.FALSE)

def display(displayVal, displayOn = False):
    if displayOn == True:
        hub.display.off()
        displayOn = False
    else:
        displayOn = True
        if isinstance(displayVal, int):
            if displayVal < 10:
                hub.display.char(str(displayVal))
            else:
                hub.display.number(int(displayVal))
        else:
            hub.display.char(displayVal)
    return displayOn
