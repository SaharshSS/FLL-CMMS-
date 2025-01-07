from pybricks.tools import wait
import Arm, Drive

def mission1():
    Arm.turnArm(65, 65)
    Drive.straight(200)
    wait(500)
    Drive.back(150)
    Arm.resetArm()

def mission2():
    Arm.turnArm(0, 0)
    wait(500)
    Arm.resetArm()

def mission3():
    Drive.turn(80)
    Arm.resetArm()
    Drive.straight(50)
    Arm.turnArm(45, -45, mode = 2)
    wait(500)
    Arm.armUp()
    Drive.turn(100)

def mission4():
    pass

def mission5():
    pass #Task 5 does not use arm or anything so its kinda useless 4 now

def mission6():
    Arm.turnArm(0, 0)
    Drive.straight(100)
    Arm.turnArm(35, 35, speed = 25)
    wait(1000)
    Drive.straight(50)
    Arm.turnArm(80, 45, speed = 25)
    wait(1000)
    Drive.straight(-150)
    Arm.resetArm()

def mission7():
    pass

def mission8():
    Arm.turnArm(0, 0)
    Drive.turn(-20)
    Drive.straight(100)
    Drive.turn(110)
    Drive.straight(100)
    Arm.resetArm()
    Drive.turn(-90)
    Drive.back(100)
    Arm.turnArm(0, 0)
    Drive.straight(150)
    Arm.turnArm(0, 77.5, 1, 7500) #Not sure if arm can reach this speed but this should be aiming to flick the mission

def mission9():
    Arm.armUp()
    Drive.straight(500)
    Drive.back(500)
    Arm.resetArm()

def mission10():
    Arm.armUp()

def mission11():
    pass

def mission12():
    Arm.armUp()    #Arm should already be up
    Drive.straight(200, speed = 250)
    Drive.back(200)

def mission13():
    Drive.turn(60)
    Arm.turnArm(45, 45)
    Drive.turn(40)

def mission14():
    pass

def mission15():
    pass

def pushups():
    while True:
        Arm.turnArm(0, -90, 2, 2500)
        wait(500)
        Arm.turnArm(-90, -90, 0, 2500)
        wait(500)
