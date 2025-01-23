from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor

try:
    armMid = Motor(Port.F) #Motor ports 1
    armBase = Motor(Port.D, Direction.COUNTERCLOCKWISE)
except OSError:
    print("Using alternative arm ports") #Newer setup
    armMid = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    armBase = Motor(Port.E)

def turn(midAngle, baseAngle, mode = 0, speed = 1750):   #Rotate arm
    if not mode:
        armMid.run_target(speed, midAngle, wait = False)
        armBase.run_target(speed, baseAngle)
    elif mode == 1:
        armMid.run_target(speed, midAngle)
        armBase.run_target(speed, baseAngle)
    elif mode == 2:
        armBase.run_target(speed, midAngle)
        armMid.run_target(speed, baseAngle)
    else:
        armBase.run_target(speed, midAngle, wait = False)
        armMid.run_target(speed, baseAngle, wait = False)

def reset():                                     #Arm reset to default position
    turn(0, 90, 1, 2500)

def up():                                        #Arm set to "Up" position
    turn(90, 90, 1, 2500)

def hook():
    turn(45, -45, 2, 2500)

def disable():
    armMid.stop()
    armBase.stop()
    
reset()
disable()

print("Arm.py loaded")
