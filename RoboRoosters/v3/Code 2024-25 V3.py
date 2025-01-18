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

left.control.target_tolerances(360, 5)
right.control.target_tolerances(360, 5)

armMid.control.target_tolerances(180, 5)
armBase.control.target_tolerances(180, 5)


drive = DriveBase(left, right, wheel_diameter=56.34, axle_track=139.7)

colorSensor = ColorSensor(Port.C)

def setup():
    hub.speaker.beep()
    hub.display.icon(Icon.CIRCLE)
    drive.reset()
    print("")
    print("Version " + str(version))
    print("Battery Current " + str(hub.battery.current()))
    v = hub.battery.voltage()
    print("Battery voltage " + str(v) + "v / Percentage " + str(percentFromVolt(v)) + "%")
    print("Name " + str(hub.system.name()))
    drive.use_gyro(True)
    drive.settings(straight_speed = 750, straight_acceleration = 1000, turn_rate = 750, turn_acceleration = 1000)
    hub.imu.reset_heading(0)
    while not hub.imu.ready():
        wait(100)
        hub.display.icon(Icon.FALSE)
    resetArm()
    left.run_target(5000, 0, wait = False)
    right.run_target(5000, 0, wait = False)
    armMid.stop()
    armBase.stop()
    while not left.done() or not right.done():
        wait(100)
    left.stop()
    right.stop()


def turnArm(midAngle, baseAngle, mode = 0, speed = 1000):
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
    turnArm(0, 77.5, 2, 2500)
    
def armUp():
    turnArm(-80, 77.5, 2, 2500)

def circle():
    drive.curve(300, 360)

def smoothArmAdvance(ammount, ratio = 1):
    turnArm(0, 0)
    wait(500)
    for i in range(ammount):
        drive.straight(ratio)
        if i < 90:
            turnArm(i, 0, 0, 10)
        else:
            turnArm(90, i-90, 0, 10)

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
    drive.turn(45)
    drive.straight(300)
    drive.turn(-45)
    drive.straight(420)
    turnArm(-55, 55, 3, 100)
    drive.turn(-90)
    drive.straight(150)
    resetArm()
    drive.straight(-100)
    drive.turn(-90)
    drive.straight(420)
    drive.turn(45)
    drive.straight(300)

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
    armUp()
    drive.turn(45)
    drive.straight(200)
    drive.turn(-45)
    drive.straight(500)
    drive.turn(180)
    drive.straight(-300)
    drive.turn(-90)
    turnArm(90, -10, 4, 50)
    wait(4000)
    resetArm()
    armUp()
    drive.straight(-100)
    drive.turn(90)
    drive.straight(500)
    drive.turn(45)
    drive.straight(250)

def task4():
    pass

def task5():
    armUp()
    drive.turn(-45)
    drive.straight(285)
    drive.turn(-45)
    drive.straight(260)
    drive.turn(40)
    drive.straight(480)
    drive.curve(150, -45)
    wait(100)
    drive.curve(150, 270)
    drive.straight(300)
    drive.turn(-45)
    drive.straight(450)
    drive.turn(-45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(200)
    resetArm()
    wait(200)

def task6():
    drive.straight(100)
    drive.turn(90)
    drive.straight(390)
    turnArm(0, 0, mode = 4)
    drive.turn(-90)
    drive.straight(100)
    turnArm(-45, 45, speed = 25, mode = 4)
    wait(1000)
    drive.straight(50)
    turnArm(-62.5, 45, speed = 25, mode = 4)
    wait(1000)
    drive.straight(-50)
    drive.turn(90)
    drive.straight(150)
    drive.turn(-90)
    drive.straight(200)
    drive.straight(-200)
    drive.turn(-90)
    drive.straight(250)
    drive.turn(-45)
    drive.straight(400)

def task7():
    '''
    turnArm(0, 0, mode = 2)
    drive.turn(-45)
    drive.straight(500)
    turnArm(0, 45, 2, 2500)
    drive.straight()
    drive.straight(-500)
    '''
    '''
    drive.turn(-90)
    drive.straight(250)
    drive.turn(45)
    drive.straight(500)
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
    '''
    drive.straight(-100)
    drive.turn(45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(200)
    turnArm(45, 0)
    drive.straight(100)
    armUp()
    drive.straight(-200)
    drive.turn(90)
    drive.straight(50)
    drive.turn(-90)
    drive.straight(200)
    drive.straight(-200)
    drive.turn(-90)
    drive.straight(250)
    drive.turn(-45)
    drive.straight(350)

def task8():
    turnArm(0, 0)
    drive.straight(-160)
    drive.turn(-90)
    drive.straight(500)
    resetArm()
    drive.straight(50)
    armUp()
    drive.straight(100)
    drive.straight(-600)

def task9():
    armUp()
    drive.turn(-45)
    drive.straight(600)
    drive.straight(-600)

def task10():
    resetArm()
    drive.turn(-90)
    drive.straight(250)
    drive.turn(45)
    drive.straight(500)
    drive.turn(45)
    drive.straight(300)
    drive.turn(-30)
    drive.straight(175)
    for i in range(5):
        drive.straight(75)
        armUp()
        resetArm()
        drive.straight(-75)
    drive.straight(-100)
    drive.turn(-150)
    drive.straight(300)
    drive.turn(-45)
    drive.straight(500)
    drive.turn(-45)
    drive.straight(350)

def task11():
    pass

def task12():
    armUp()
    wait(10000)
    drive.turn(-45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(400)
    drive.turn(45)
    drive.straight(400)
    wait(500)
    drive.straight(-400)
    drive.turn(135)
    drive.straight(370)
    drive.turn(-45)
    drive.straight(200)


def task13():
    armUp()
    drive.turn(-45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(500)
    drive.turn(135)
    drive.straight(-75)
    turnArm(20, 0)
    drive.straight(100)
    resetArm()
    drive.straight(150)
    turnArm(-25, 77.5, 2, 100)
    drive.straight(-100)
    drive.turn(45)
    drive.straight(525)
    drive.turn(-45)
    drive.straight(100)

def task14():
    pass

def task15():
    armUp()
    drive.straight(100)
    drive.turn(90)
    drive.straight(200)
    resetArm()
    drive.straight(200)
    drive.straight(-200)
    armUp()
    drive.turn(45)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(400)
    drive.straight(-400)
    drive.turn(-135)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(200)
    drive.turn(-45)
    drive.straight(200)

def SAATest():
    smoothArmAdvance(100)
tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15, SAATest, armUp, colorSensor.color]
inputs = []
inputCount =  0
menuindex = 0

def constrain(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def percentFromVolt(voltage):
    voltage = voltage - 6.2
    voltage = voltage * 200
    voltage = constrain(voltage, 0, 100)
    return voltage

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
                dispOn = 3
                hub.speaker.beep()
            elif Button.RIGHT in pressed:
                hub.speaker.beep()
                menuindex += 1
                dispOn = 3
            menuindex = constrain(menuindex, 0, len(tasks))
            if dispOn <= 2:
                dispOn = dispOn + 1
                hub.display.off()
            else:
                if menuindex >= 10:
                    hub.display.number(menuindex)
                elif menuindex == 0:
                    hub.display.char("A")
                else: 
                    hub.display.char(str(menuindex))
                dispOn = 0
            wait(100)
        if menuindex == 0:
            print("")
            print("Going across")
            across()
            drive.straight(0, then=Stop.COAST) #Disable gyroscope
        else:
            try:
                resetArm()
                print("")
                print("Running task " + str(menuindex))
                v = hub.battery.voltage()/1000
                print("Battery voltage " + str(v) + "v / Percentage " + str(percentFromVolt(v)) + "%")
                x = tasks[menuindex-1]()
                drive.stop() #Disable gyroscope
                resetArm()
                armMid.stop()
                armBase.stop()
                print("")
                print("Task " + str(menuindex) + " finished, returned " + str(x))
                if not x == None:
                    hub.display.text(str(x), 150, 25)
                v2 = hub.battery.voltage()/1000
                print("Battery voltage " + str(v2) + "v / Percentage" + str(percentFromVolt(v2)) + "%")
                change = round((v2-v)*1000)/1000
                if change > 0:
                    print("Battery change +" + str(round((v2-v)*1000)/1000) + "v")
                elif change < 0:
                    print("Battery change +" + str(round((v2-v)*1000)/1000) + "v")
            except TypeError:
                print("TypeError")
                print("Put function in another function, eg: def runfunc: run(x, y)")
main()
