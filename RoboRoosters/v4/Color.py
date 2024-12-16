from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
color = ColorSensor(port=Port.C)
color.lights.off()
def getColor():
    return color.color()
def getBrightness():
    return color.ambient()
