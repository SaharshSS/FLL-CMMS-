from pybricks.tools import wait
import Arm, Console, Color, Drive

def mission1():
    Arm.turnArm(55, 55, 3)
    Drive.straight(150)
    Drive.back(150)
    Arm.turnArm(0, 0)
    Drive.back(-200)
    Arm.resetArm()

def mission2():
    Arm.resetArm()
    Arm.turnArm(0, 0)
    wait(500)
    Arm.resetArm()

def mission3():
    Arm.turnArm(0, 0, 2, 50)
    wait(500)
    Arm.resetArm()

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
    Drive.straight(200)
    Drive.back(200)
    Arm.resetArm()

def mission10():
    resetArm()
    Drive.straight(100)
    turnArm(20, 77.5, 1, 2500)
    Drive.straight(100)
    turnArm(45, 77.5, 1, 2500)
    Drive.straight(100)
    Arm.armUp()
    Drive.back(300)

def mission11():
    pass

def mission12():
    Arm.armUp()    #Arm should already be up
    Drive.straight(200, speed = 250)
    Drive.back(200)

def mission13():
    Arm.turnArm(0, -5, 1, 150)
    Drive.straight(100)
    Arm.turnArm(0, 35, 2, 150)
    Drive.straight(50)
    Arm.resetArm()
    Drive.straight(150)
    Arm.armUp()
    Drive.back(165)
    Drive.turn(-45)
    Arm.turnArm(-40, 55, 1)
    Drive.back(200)
    Arm.resetArm()

def mission14():
    pass

def mission15():
    Arm.armUp()
    Drive.turn(90)
    Drive.straight(200)
    Arm.resetArm()
    Drive.straight(500)
    Drive.straight(-250)
    Arm.armUp()
    Drive.turn(45)
    Drive.straight(250)
    Drive.turn(-45)
    Drive.straight(600)
    Drive.straight(-400)
    Drive.turn(-90)
    Drive.straight(250)
    Drive.turn(90)
    Drive.straight(850)
    Drive.turn(45)
    Drive.straight(100)

def pushups():
    while True:
        Arm.turnArm(0, -90, 2, 2500)
        wait(500)
        Arm.turnArm(-90, -90, 0, 2500)
        wait(500)

def TrackLine(Distance, NewDistance=0, NewDirection=1):
    if NewDistance >= Distance:
        Drive.straight(0, Stop.COAST)
        return

    if Color.getColor() == "White":
        NewDirection = NewDirection * -1
        while Color.getColor() != "White":
            Drive.curve(20 * NewDirection, 1, Stop.COAST)
        Drive.straight(1, Stop.COAST)
        NewDistance += 0.5
    TrackLine(Distance, NewDistance, NewDirection)

def TrackLine1(Distance = 100, Direction=True):
    curve_direction = 20 if Direction else -20
    while NewDistance < Distance:
        if Color.getColor() == "White":
            Drive.straight(1, Stop.COAST)
        else:
            Drive.curve(curve_direction, 1, Stop.COAST)
        NewDistance += 1
