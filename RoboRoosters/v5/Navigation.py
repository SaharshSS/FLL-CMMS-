from pybricks.tools import wait
import Drive, Arm, Missions

def acrossL():
    Drive.curve(200, -90)
    wait(100)
    Drive.straight(1200)
    Drive.curve(200, -65)

def acrossR():
    Drive.curve(200, 90)
    wait(100)
    Drive.straight(1200)
    Drive.curve(200, 65)

def MovementA():
    Drive.turn(-50)
    Missions.mission9()
    Drive.turn(50)
    Arm.turnArm(10, -10, 2)
    Drive.straight(500)
    Drive.turn(100)
    Arm.armUp()

def MovementB():
    Drive.turn(20)
    Drive.straight(550)
    Drive.turn(-110)
    Missions.mission1()
    Drive.turn(45)
    Drive.straight(170)
    Missions.mission2()
    Arm.armUp()
    Drive.turn(45)
    Drive.straight(200)
    Missions.mission3()
    Drive.back_square()
    Drive.straight(250)
    Drive.turn(-90)
    Drive.straight(550, speed = 400) #It curves on this path 4 some reason
    Drive.turn(-45)
    Arm.resetArm()
    Drive.straight(200)
    Missions.mission10()
    Drive.back(200)
    Drive.turn(45)
    Drive.straight(650, speed = 400) #It curves on this path 4 some reason
    Drive.turn(65)
    Drive.straight(550, speed = 400) #It curves on this path 4 some reason
    
def MovementC():
    Drive.turn(75)
    Drive.straight(450)
    Drive.turn(-75)
    Missions.mission6() #Idk Mission 6 would be blank I guess
    Missions.mission7()
    Drive.turn(-180)
    Drive.straight(250)
    Drive.turn(-90)
    Missions.mission15()

def MovementD():
    Drive.turn(-52) #Rly precise measurement for dis one
    Drive.straight(110)
    Drive.turn(142)
    Drive.straight(825)
    Drive.turn(-45)
    Missions.mission(12)
