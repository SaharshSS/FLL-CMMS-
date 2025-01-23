from pybricks.tools import wait
from pybricks.parameters import Stop
import Arm, Drive

def mission1():
    Arm.turn(52.5, 52.5, mode = 3)
    wait(100)
    Drive.straight(300, then=Stop.COAST_SMART)
    Drive.back(150)
    Arm.reset()

def mission2():
    Drive.turn(-10)
    Arm.hook()
    wait(500)
    Arm.reset()
    Arm.up()

def mission3():
    Drive.turn(90, wait=False)
    Arm.reset()
    Drive.straight(50, wait=False)
    wait(200)
    Arm.turn(25, -10, 2, 2500)
    Drive.turn(-20, wait=False)
    Arm.reset()
    Drive.turn(110, wait=False)
    Arm.up()

def mission4():
    pass

def mission5():
    Arm.hook()
    Drive.back(75)
    Drive.turn(25)
    Arm.reset()
    Drive.turn(-70)


def mission6():
    Arm.turn(10, 0)
    Drive.straight(175, then=Stop.COAST_SMART)
    Drive.back(25, wait=False)
    Arm.turn(45, 45, mode=3)
    Drive.straight(50, speed=50)
    wait(500)
    Drive.back(25)
    Drive.turn(-50)
    Arm.disable()
    Drive.back(100)
    Drive.turn(5)

def mission7():
    pass

def mission8():
    Arm.hook()
    Arm.disable()
    Drive.back(150)
    Arm.up()
    for i in range(4):
        Arm.up()
        Drive.straight(150)
        Arm.turn(20, 90)
        Drive.back(300)


def mission9():
    Drive.straight(500, wait=False)
    Arm.up()
    Drive.back(300)

def mission10():
    Drive.turn(-15, wait = False)
    Arm.turn(65, 65, 0, 2500)
    wait(1500)
    Drive.turn(15)

def mission11():
    pass

def mission12():
    Drive.straight(200, speed = 250)
    Drive.back(200)

def mission13():
    Drive.back(150, wait=False)
    Arm.turn(5, 0, mode = 2)
    Arm.disable()
    Drive.straight(300, speed=100)
    Arm.reset()
    Arm.up()
    Drive.turn(-90)
    Drive.back(25, wait=False)
    Arm.hook()
    Drive.turn(45, speed=500)
    Drive.turn(45)

def mission14():
    Drive.back(100, wait=False)
    Arm.turn(20, 20)
    Drive.straight(150)
    Arm.turn(30, 95, 1, 500)
    Drive.front_square()
    Drive.back(50)

def mission15():
    Drive.straight(500)
    Drive.back(300)
    Drive.turn(-90)
    Drive.back_square()

print("Missions.py loaded")
