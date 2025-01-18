from pybricks.tools import wait
import Arm, Drive

def mission1():
    Arm.turnArm(52.5, 52.5)
    wait(500)
    Drive.straight(200)
    Drive.back(150)
    Arm.resetArm()

def mission2():
    Drive.turn(-10)
    Arm.turnArm(0, 0)
    wait(500)
    Arm.resetArm()
    Arm.armUp()

def mission3():
    Drive.turn(90)
    Arm.resetArm()
    Drive.straight(50)
    Arm.turnArm(0, 0, 2, 2500)
    Drive.turn(-20)
    Arm.resetArm()
    Arm.armUp()
    Drive.turn(110)

def mission4():
    pass

def mission5():    
    Arm.hook()
    Drive.back(75)
    Drive.turn(30)
    Arm.resetArm()
    Drive.turn(-75)


def mission6():
    Arm.turnArm(10, 0)
    Drive.straight(175)
    Arm.turnArm(45, 45)
    Arm.disableArm()
    Drive.straight(50)
    Drive.turn(-65, speed=100)
    Drive.back(100)
    Drive.turn(20)

def mission7():
    pass

def mission8():
    Arm.turnArm(0, 25)
    Drive.back(200)
    Arm.resetArm()
    for i in range(4):
        Arm.armUp()
        Drive.straight(200)
        Arm.turnArm(20, 90)
        Drive.back(300)

def mission9():
    Arm.armUp()
    Drive.straight(500)
    Drive.back(300)

def mission10():
    Drive.turn(-15)
    Arm.turnArm(70, 70, 1, 2500)
    wait(1500)
    Drive.turn(15)

def mission11():
    pass

def mission12():
    Drive.straight(200, speed = 250)
    Drive.back(200)

def mission13():
    Drive.back(100)
    Arm.turnArm(0, 10)
    wait(50)
    Arm.disableArm()
    Drive.straight(300, speed=100)
    Arm.resetArm()
    Arm.armUp()
    Drive.turn(-90)
    Drive.back(50)
    Arm.hook()
    Drive.turn(-45, speed=250)
    Drive.turn(45)

def mission14():
    pass

def mission15():
    Drive.straight(500)
    Drive.back(300)
    Drive.turn(-90)
    Drive.back_square()
    
