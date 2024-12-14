from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor
from pybricks.tools import wait
import Arm
import Console

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

left.control.target_tolerances(360, 5)
right.control.target_tolerances(360, 5) 

drive = DriveBase(left, right, wheel_diameter=56.34, axle_track=139.7)

drive.use_gyro(True)
drive.settings(straight_speed = 750, straight_acceleration = 1000, turn_rate = 750, turn_acceleration = 1000)

print("Tasks.py loaded")

def across(direction = 0):
    if direction:
        drive.curve(200, 90)
        wait(100)
        drive.straight(1200)
        drive.curve(200, 65)
    else:
        drive.curve(200, -90, Stop.HOLD)
        wait(100)
        drive.straight(1200)
        drive.curve(200, -65)
def stop():
    drive.stop()

def task1():
    drive.turn(45)
    drive.straight(300)
    drive.turn(-45)
    drive.straight(420)
    Arm.turnArm(55, 55, 3, 100)
    drive.turn(-90)
    drive.straight(150)
    Arm.resetArm()
    drive.straight(-100)
    drive.turn(-90)
    drive.straight(420)
    drive.turn(45)
    drive.straight(300)

def task2():
    Arm.resetArm()
    drive.turn(45)
    drive.straight(200)
    drive.turn(-45)
    drive.straight(500)
    drive.turn(-45)
    drive.straight(20)
    Arm.turnArm(0, 0)
    wait(1000)
    Arm.resetArm()
    drive.straight(-20)
    drive.turn(45)
    drive.straight(-500)
    drive.turn(45)
    drive.straight(-200)

def task3():
    Arm.armUp()
    drive.turn(45)
    drive.straight(200)
    drive.turn(-45)
    drive.straight(500)
    drive.turn(180)
    drive.straight(-300)
    drive.turn(-90)
    Arm.turnArm(0, 0, 3, 50)
    wait(4000)
    Arm.resetArm()
    Arm.armUp()
    drive.straight(-100)
    drive.turn(90)
    drive.straight(500)
    drive.turn(45)
    drive.straight(250)

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
    Arm.resetArm()
    wait(200)

def task6():
    drive.straight(100)
    drive.turn(90)
    drive.straight(390)
    Arm.turnArm(0, 0)
    drive.turn(-90)
    drive.straight(100)
    Arm.turnArm(45, 45)
    wait(1000)
    drive.straight(50)
    Arm.turnArm(62.5, 45)
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
    drive.straight(-100)
    drive.turn(45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(100)
    drive.turn(-45)
    drive.straight(200)
    Arm.turnArm(0, 45)
    drive.straight(100)
    Arm.armUp()
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

def task10():
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
        Arm.armUp()
        Arm.resetArm()
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
    Arm.armUp()
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
    Arm.armUp()
    drive.turn(-45)
    drive.straight(200)
    drive.turn(45)
    drive.straight(500)
    drive.turn(135)
    drive.straight(-75)
    Arm.turnArm(0, 20)
    drive.straight(100)
    Arm.resetArm()
    drive.straight(150)
    Arm.armUp()
    drive.straight(-100)
    drive.turn(45)
    drive.straight(525)
    drive.turn(-45)
    drive.straight(100)

def task14():
    pass

def task15():
    Arm.armUp()
    drive.straight(100)
    drive.turn(90)
    drive.straight(200)
    Arm.resetArm()
    drive.straight(200)
    drive.straight(-200)
    Arm.armUp()
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
