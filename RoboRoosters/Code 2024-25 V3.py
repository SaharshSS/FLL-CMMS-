from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.parameters import Color, Button, Port, Direction, Stop, Side, Icon
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor
from pybricks.tools import run_task, wait
from pybricks import version

hub = PrimeHub()

armMid = Motor(Port.D, Direction.COUNTERCLOCKWISE)
armBase = Motor(Port.F, Direction.COUNTERCLOCKWISE)

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

drive = DriveBase(left, right, wheel_diameter=56.34, axle_track=139.7)

colorSensor = ColorSensor(Port.C)

def setup():
    print("Hello world!")
    hub.display.icon(Icon.CIRCLE)
    drive.reset()
    print("Version " + str(version))
    drive.use_gyro(True)
    drive.settings(straight_speed = 500, straight_acceleration = 500, turn_rate = 500, turn_acceleration = 100)
    hub.imu.reset_heading(0)
    while not hub.imu.ready():
        wait(100)
        hub.display.icon(Icon.FALSE)
    resetArm()
    armMid.stop()
    armBase.stop()

def turnArm(midAngle, baseAngle, mode = 0, speed = 500):
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
        
def across():
    drive.straight(1000)

def resetArm():
    turnArm(0, 77.5, 2, 100)
    
def circle():
    drive.curve(300, 360)

def across():
    wait(100)
    pressed = []
    arrowDir = False
    while True:
        pressed = hub.buttons.pressed()
        if arrowDir:
            arrowDir = False
            hub.display.icon(Icon.ARROW_LEFT)
        else:
            arrowDir = True
            hub.display.icon(Icon.ARROW_RIGHT)
        if any(pressed):
            break
        wait(500)
    if Button.RIGHT in pressed:
        drive.curve(200, 90, Stop.HOLD)
        drive.straight(1200)
        drive.curve(200, 65)
    else:
        drive.curve(200, -90, Stop.HOLD)
        drive.straight(1200)
        drive.curve(200, -65)
def task1():
    resetArm()
    drive.turn(45)
    drive.straight(250)
    drive.turn(-45)
    drive.straight(375)
    drive.turn(-90)
    turnArm(0, -20, mode = 1, speed = 100)
    drive.straight(75)
    wait(1000)
    drive.straight(-125)
    drive.turn(90)
    drive.straight(-375)
    drive.turn(45)
    drive.straight(-300)
    resetArm()

def task2():
    resetArm()
    drive.turn(45)
    drive.straight(200)
    drive.turn(-45)
    drive.straight(500)
    drive.turn(-45)
    drive.straight(20)
    turnArm(0, 0)
    wait(1000)
    resetArm()
    drive.straight(-20)
    drive.turn(45)
    drive.straight(-500)
    drive.turn(45)
    drive.straight(-200)

def task3():
    pass

def task4():
    pass

def task5():
    resetArm()
    drive.straight(50)
    drive.turn(-90)
    drive.straight(350)
    drive.turn(45)
    drive.straight(850)
    drive.curve(100, -45)
    drive.curve(50, 270)
    drive.straight(150)
    drive.curve(100, -45)
    drive.straight(300)
    drive.turn(-45)
    drive.straight(250)
    drive.turn(45)
    drive.straight(250)

def task6():
    resetArm()
    drive.straight(280)
    drive.turn(45)
    drive.straight(200)
    drive.turn(45)
    turnArm(0, 0)
    wait(1500)
    drive.straight(145)
    turnArm(35, 0)
    wait(1000)
    drive.straight(75)
    turnArm(90, -40, 0, 75)
    wait(1000)
    turnArm(70, 10)
    wait(500)
    drive.straight(-250)
    resetArm()
    drive.turn(100)
    drive.straight(400)

def task7():
    turnArm(0, 0, mode = 4)
    drive.turn(-45)
    drive.straight(500)
    drive.straight(-500)
    resetArm()

def task8():
    turnArm(-45, 77.5)
    drive.straight(-160)
    drive.turn(-90)
    drive.straight(500)
    drive.turn(35)
    drive.turn(-35)
    drive.straight(-500)

def task9():
    turnArm(-90, 77.5, 3, 100)
    drive.turn(-45)
    drive.straight(288*2) #Im lazy
    drive.straight(288*-2) #lazy again
    resetArm()

def task10():
    resetArm()
    drive.turn(-90)
    drive.straight(250)
    drive.turn(45)
    drive.straight(950)
    drive.turn(45)
    turnArm(0, 60)
    drive.straight(75)
    turnArm(30, 60, mode=2)
    drive.straight(25)
    turnArm(60, 60, mode=2)
    drive.straight(50)
    turnArm(90, 90, mode=2)
    drive.straight(-150)
    drive.turn(-45)
    drive.straight(-950)
    drive.turn(-45)
    drive.straight(300)


def task11():
    pass

def task12():
    turnArm(-90, 77.5, 3)
    drive.turn(-45)


def task13():
    turnArm(-90, 77.5, 3, 100)
    drive.turn(-45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(500)
    drive.turn(135)
    drive.straight(-75)
    turnArm(0, 0)
    drive.straight(75)
    resetArm()
    drive.straight(150)
    turnArm(-45, 77.5, 3, 100)
    wait(500)
    drive.straight(-100)
    drive.turn(45)
    drive.straight(525)
    drive.turn(-45)
    drive.straight(200)
    resetArm()

def task14():
    pass

def task15():
    resetArm()
    drive.straight(800)
    drive.straight(-200)

tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15]
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
                if menuindex >= 10:
                    hub.display.number(menuindex)
                elif menuindex == 0:
                    hub.display.char("A")
                else: 
                    hub.display.char(str(menuindex))
                hub.speaker.beep()
                break
            if Button.LEFT in pressed:
                menuindex -= 1
                dispOn = False
                hub.speaker.beep()
            elif Button.RIGHT in pressed:
                hub.speaker.beep()
                menuindex += 1
                dispOn = False
            menuindex = constrain(menuindex, 0, len(tasks))
            if dispOn:
                dispOn = False
                hub.display.off()
            else:
                if menuindex >= 10:
                    hub.display.number(menuindex)
                elif menuindex == 0:
                    hub.display.char("A")
                else: 
                    hub.display.char(str(menuindex))
                dispOn = True
            wait(100)
        if menuindex == 0:
            print("Going across")
            across()
            drive.straight(0, then=Stop.COAST) #Disable gyroscope
        else:
            try:
                print(menuindex)
                print(tasks[menuindex-1])
                tasks[menuindex-1]()
                drive.straight(0, then=Stop.COAST) #Disable gyroscope
                armMid.stop()
                armBase.stop()
            except TypeError:
                print("TypeError")
                print("Put function in another function, eg: def runfunc: run(x, y)")
main()
