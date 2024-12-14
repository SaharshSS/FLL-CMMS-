from pybricks.hubs import PrimeHub
from pybricks import version
import Tasks, Arm

import Battery

hub = PrimeHub()

print("Console.py loaded")


def dispNumber(number):
    if number < 10 and number >= 0:
        hub.display.char(str(int(number)))
    else:
        hub.display.number(number)

def Stats():
    print("")
    print("Version " + str(version))
    print("Battery Current " + str(Battery.current()))
    v = Battery.voltage()
    print("Battery voltage " + str(v) + "v / Percentage " + str(Battery.percentage(v)) + "%")
    print("Name " + str(hub.system.name()))

def Run(index, function):
    Arm.resetArm()
    dispNumber(index)
    print("")
    print("Running task " + str(index))
    v = Battery.voltage()
    print("Battery voltage " + str(v) + "v / Percentage " + str(Battery.percentage(v)) + "%")
    x = None
    x = function()
    print("Task " + str(index) + " finished, returned " + str(x))
    if not x == None:
        hub.display.text(str(x), 150, 25)
    v2 = Battery.voltage()
    print("")
    print("Battery voltage " + str(v2) + "v / Percentage" + str(Battery.percentage(v2)) + "%")
    Arm.resetArm()
    Arm.disableArm()
    Tasks.stop()
