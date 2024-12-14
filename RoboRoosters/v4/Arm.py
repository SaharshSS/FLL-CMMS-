from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor

print("Arm.py loaded")


armMid = Motor(Port.F)                              #Define motors
armBase = Motor(Port.D, Direction.COUNTERCLOCKWISE)

armMid.control.target_tolerances(180, 5)            #Make arm tollerances more precise
armBase.control.target_tolerances(180, 5)

def turnArm(midAngle, baseAngle, mode = 0, speed = 1000):   #Rotate arm
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

def resetArm():                                     #Arm reset to default position
    turnArm(0, 77.5, 1, 2500)

def armUp():                                        #Arm set to "Up" position
    turnArm(80, 77.5, 1, 2500)

def disableArm():
    resetArm()
    armMid.stop()
    armBase.stop()
