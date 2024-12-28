from pybricks.parameters import Icon
from pybricks.hubs import PrimeHub
hub = PrimeHub
hub.display.icon(Icon.FALSE)
displayOn = False

def display(displayVal, displayForceOn = False):
    if displayForceOn == True:
        displayOn = False
    if displayOn = True:
        hub.display.off()
        break
    if isinstance(displayVal, int):
        if displayVal > 9:
            hub.display.number(displayVal)
            break
        displayVal = str(displayVal)
    hub.display.char(displayVal)
