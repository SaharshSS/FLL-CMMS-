from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor
from pybricks.tools import wait
import Arm, Console, Color

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

left.control.target_tolerances(360, 5)
right.control.target_tolerances(360, 5) 

drive = DriveBase(left, right, wheel_diameter=56.34, axle_track=139.7)

drive.use_gyro(True)
drive.settings(straight_speed = 750, straight_acceleration = 750, turn_rate = 750, turn_acceleration = 1000)

print("Tasks.py loaded")

def acrossr():
    drive.curve(200, 90)
    wait(100)
    drive.straight(1200)
    drive.curve(200, 65)

def acrossl():
    drive.curve(200, -90)
    wait(100)
    drive.straight(1200)
    drive.curve(200, -65)

def Stop():
    drive.stop()

def task1():
    Arm.turnArm(55, 55, 3)
    drive.turn(45)
    drive.straight(250)
    drive.turn(-45)
    drive.straight(475)
    drive.straight(-100)
    drive.turn(-90)
    drive.straight(150)
    drive.straight(-150)
    drive.turn(90)
    drive.straight(-50)
    drive.turn(-45)
    drive.straight(200)
    Arm.turnArm(0, 0)
    wait(500)
    drive.straight(-200)
    Arm
    drive.turn(-135)
    drive.straight(500)
    drive.turn(45)
    drive.straight(200)

def task2():
    Arm.resetArm()
    drive.turn(45)
    drive.straight(200)
    drive.turn(-45)
    drive.straight(500)
    drive.turn(-45)
    drive.straight(100)
    Arm.turnArm(0, 0)
    wait(1000)
    Arm.resetArm()
    drive.straight(-100)
    drive.turn(45)
    drive.straight(-500)
    drive.turn(45)
    drive.straight(-200)

def task3():
    drive.turn(45)
    drive.straight(200)
    drive.turn(-45)
    drive.straight(500)
    drive.turn(180)
    drive.straight(-300)
    drive.turn(-90)
    Arm.turnArm(0, 0, 2, 50)
    drive.turn(90)
    Arm.resetArm()
    Arm.armUp()
    drive.straight(800)
    drive.turn(45)
    drive.straight(200)

def task4():
    pass

def task5():
    Arm.armUp()
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

def task6():
    drive.straight(100)
    drive.turn(90)
    drive.straight(350)
    Arm.turnArm(0, 0)
    drive.turn(-90)
    drive.straight(100)
    Arm.turnArm(35, 35, speed = 25)
    wait(1000)
    drive.straight(50)
    Arm.turnArm(80, 45, speed = 25)
    wait(1000)
    drive.straight(-50)
    drive.turn(-90)
    drive.straight(150)
    drive.turn(-45)
    drive.straight(400)

def task7():
    drive.straight(-100)
    drive.turn(45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(200)
    Arm.turnArm(0, 45, 2)
    drive.straight(100)
    Arm.armUp()
    drive.straight(-50)
    drive.turn(-125)
    drive.straight(600)

def task8():
    Arm.turnArm(0, 0)
    drive.straight(-160)
    drive.turn(-90)
    drive.straight(500)
    Arm.resetArm()
    drive.straight(50)
    Arm.armUp()
    drive.straight(100)
    drive.straight(-600)

def task9():
    Arm.armUp()
    drive.turn(-45)
    drive.straight(600)
    drive.straight(-600)
    Arm.resetArm()
    drive.turn(45)
    drive.stop()
    print("3 seconds to put in squid")
    wait(3000)
    drive.turn(-45)
    drive.straight(250)
    drive.turn(45)
    drive.straight(400)
    drive.turn(-90)
    drive.straight(300)
    drive.turn(-45)
    drive.turn(225)
    drive.straight(300)
    drive.turn(90)
    drive.straight(400)
    drive.turn(-45)
    drive.straight(150)

def task10():
    drive.turn(-90)
    drive.straight(250)
    drive.turn(45)
    drive.straight(525)
    drive.turn(45)
    drive.straight(325)
    drive.turn(-35)
    for i in range(5):
        drive.straight(100)
        Arm.armUp()
        wait(200)
        drive.straight(-100)
        Arm.resetArm()
    drive.straight(-35)
    drive.turn(-145)
    drive.straight(325)
    drive.turn(-45)
    drive.straight(525)
    drive.turn(-45)
    drive.straight(350)

def task11():
    pass

def task12():
    Arm.turnArm(100, 77.5, 1, 2500)
    wait(2000)
    drive.turn(-45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(450)
    drive.turn(45)
    drive.straight(200)
    Arm.armUp()
    wait(500)
    drive.straight(-275)
    drive.turn(-225)
    drive.straight(370)
    drive.turn(-45)
    drive.straight(200)


def task13():
    Arm.armUp()
    drive.turn(-45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(500)
    drive.turn(135)
    drive.straight(-75)
    Arm.turnArm(0, -5, 1, 150)
    drive.straight(100)
    Arm.turnArm(35, 0, 2, 150)
    drive.straight(50)
    Arm.resetArm()
    drive.straight(150)
    Arm.armUp()
    drive.straight(-165)
    drive.turn(-45)
    Arm.turnArm(-40, 55, 1)
    drive.straight(-200)
    Arm.armUp()
    drive.straight(200)
    drive.turn(90)
    drive.straight(525)
    drive.turn(-45)
    drive.straight(100)

def task14():
    pass

def task15():
    Arm.armUp()
    drive.turn(90)
    drive.straight(200)
    Arm.resetArm()
    drive.straight(500)
    drive.straight(-250)
    Arm.armUp()
    drive.turn(45)
    drive.straight(250)
    drive.turn(-45)
    drive.straight(600)
    drive.straight(-400)
    drive.turn(-90)
    drive.straight(250)
    drive.turn(90)
    drive.straight(850)
    drive.turn(45)
    drive.straight(100)

def pushups():
    while True:
        Arm.turnArm(0, -90, 2, 2500)
        wait(500)
        Arm.turnArm(-90, -90, 0, 2500)
        wait(500)

def TrackLine(Distance, NewDistance=0, NewDirection=1):
    if NewDistance >= Distance:
        drive.straight(0, Stop.COAST)
        return

    if Color.getColor() == "White":
        NewDirection = NewDirection * -1
        while Color.getColor() != "White":
            drive.curve(20 * NewDirection, 1, Stop.COAST)
        drive.straight(1, Stop.COAST)
        NewDistance += 0.5
    TrackLine(Distance, NewDistance, NewDirection)

def TrackLine1(Distance = 100, Direction=True):
    curve_direction = 20 if Direction else -20
    while NewDistance < Distance:
        if Color.getColor() == "White":
            drive.straight(1, Stop.COAST)
        else:
            drive.curve(curve_direction, 1, Stop.COAST)
        NewDistance += 1
