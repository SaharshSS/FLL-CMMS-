from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.parameters import Color, Button, Port, Direction, Stop, Side, Icon
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor
from pybricks.tools import run_task, wait
from pybricks import version

hub = PrimeHub()

armBase = Motor(Port.D)
armMid = Motor(Port.F, Direction.COUNTERCLOCKWISE)

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

drive = DriveBase(left, right, wheel_diameter=142, axle_track=450)

colorSensor = ColorSensor(Port.C)
try:
    distance = UltrasonicSensor(Port.E)
except OSError:
    print("No distance sensor connected")

def setup():
    print("Hello world!")
    hub.display.icon(Icon.PAUSE)
    drive.reset()
    print("Version " + str(version))
    drive.use_gyro(True)
    drive.settings(straight_speed = 2000, straight_acceleration = 4000, turn_rate = 500, turn_acceleration = 100)
    hub.imu.reset_heading(0)
    turnArm(0, 0)

def turnArm(angle1, angle2, mode = 0, speed = 500):
    if not mode:
        armBase.run_target(speed, angle2, wait = False)
        armMid.run_target(speed, angle2)
        while not armBase.done():
            wait(50)
    elif mode == 1:
        armBase.run_target(speed, angle1)
        armMid.run_target(speed, angle2)
    elif mode == 2:
        armMid.run_target(speed, angle1)
        armBase.run_target(speed, angle2)
    else:
        armMid.run_target(speed, angle1, wait = False)
        armBase.run_target(speed, angle2, wait = False)
        
def across():
    drive.straight(1000)

def resetArm():
    turnArm(45, 45, 1, 100)
    turnArm(0, 0, 2, 100)
    
def circle():
    drive.curve(300, 360)

def task9():
    turnArm(-90, 0)
    drive.turn(-45)
    drive.straight(288*2) #Im lazy
    drive.straight(288*-2) #lazy again

def task10():
    turnArm(-90, 0)
    drive.turn(-90)
    drive.straight(200)
    drive.turn(45)
    drive.straight(288*2)
    drive.turn(45)
    drive.straight(200)
    drive.straight(-200)
    drive.turn(-45)
    drive.straight(-288*2)
    drive.turn(-45)
    drive.straight(-200)

tasks = [across, resetArm, circle, task9]
inputs = []
inputCount =  0
menuindex = 0

def constrain(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def TrackLine(Distance, NewDistance=0, NewDirection=1):
    if NewDistance >= Distance:
        drive.straight(0, Stop.COAST)
        return

    if colorSensor.color() == "White":
        NewDirection = NewDirection * -1
        while colorSensor.color() != "White":
            drive.curve(20 * NewDirection, 1, Stop.COAST)
        drive.straight(1, Stop.COAST)
        NewDistance += 0.5

    TrackLine(Distance, NewDistance, NewDirection)

def TrackLine1(Distance, Direction=True):
    curve_direction = 20 if Direction else -20
    while NewDistance < Distance:
        if colorSensor.color() == "White":
            drive.straight(1, Stop.COAST)
        else:
            drive.curve(curve_direction, 1, Stop.COAST)
        NewDistance += 1

def main():
    setup()
    hub.speaker.beep()
    global menuindex, inputCount
    hub.system.set_stop_button(Button.BLUETOOTH)
    while True:
        pressed = []
        dispOn = False
        if len(tasks) == 0:
            print("Empty tasks list")
            print("Add items to tasks list to run")
            break
        while True:
            pressed = hub.buttons.pressed()
            if Button.CENTER in pressed:
                hub.display.char(str(menuindex))
                hub.speaker.beep()
                break
            if Button.LEFT in pressed:
                menuindex -= 1
                hub.speaker.beep()
            elif Button.RIGHT in pressed:
                hub.speaker.beep()
                menuindex += 1
            menuindex = constrain(menuindex, 1, len(tasks))
            if dispOn:
                dispOn = False
                hub.display.off()
            else:
                hub.display.char(str(menuindex))
                dispOn = True
            wait(100)
        try:
            print(menuindex)
            print(tasks[menuindex-1])
            tasks[menuindex-1]()
            drive.straight(0, then=Stop.COAST) #Disable gyroscope
        except TypeError:
            print("TypeError")
            print("Put function in another function, eg: def runfunc: run(x, y)")
main()
