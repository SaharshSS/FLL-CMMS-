from pybricks.tools import wait
from pybricks.parameters import Stop
import Drive, Arm, Missions

def acrossL():
    Drive.curve(200, -90, then=Stop.COAST_SMART)
    Drive.straight(1200, then=Stop.COAST_SMART)
    Drive.curve(200, -65)

def acrossR():
    Drive.curve(200, 90, then=Stop.COAST_SMART)
    Drive.straight(1200, then=Stop.COAST_SMART)
    Drive.curve(200, 65)

def MovementA():
    '''
    Drive.straight(20)
    Drive.turn(-90)
    Drive.straight(325)
    '''
    Drive.curve(20, -90, then=Stop.COAST_SMART, wait=False)
    Arm.up()
    Drive.straight(305)
    Drive.turn(-30)
    Arm.reset()
    Drive.turn(75)
    Arm.up()
    Drive.turn(-45)
    Drive.straight(200)
    Drive.turn(-45)
    Drive.back(400)
    Drive.turn(-45)
    Drive.back(300)
    Drive.turn(65)
    Drive.back(200)
    Drive.turn(-70)
    Drive.back(150, then=Stop.COAST_SMART)
    Drive.back_square()
    '''
    Drive.straight(250)
    Drive.turn(90)
    Drive.straight(810)
    '''
    Drive.curve(250, 90, then=Stop.COAST_SMART)
    Drive.straight(560)
    Drive.turn(90)
    Missions.mission14()
    '''
    Drive.straight(-125)
    Drive.turn(90)
    Drive.back(500)
    '''
    Drive.curve(-75, -90, then=Stop.COAST_SMART)
    '''
    Drive.back(425)
    Drive.turn(-90)
    Drive.back(400)
    '''
    Drive.back(400, speed=400)
    Drive.turn(180)
    Drive.straight(200)
    Arm.up()
    Drive.curve(-150, -90, then=Stop.COAST_SMART)
    Drive.back(300, then=Stop.COAST_SMART)
    Drive.curve(-150, -45, then=Stop.COAST_SMART)
    Drive.back(300)
    
def MovementB():
    Drive.turn(20)
    Drive.straight(575)
    Arm.hook()
    Drive.turn(250) #To knock over that one thing
    Missions.mission1()
    Drive.turn(45)
    Drive.straight(150)
    Missions.mission2()
    Arm.up()
    Drive.turn(55)
    Drive.straight(200, then=Stop.COAST_SMART)
    Drive.front_square()
    Missions.mission3()
    Drive.back_square()
    Drive.straight(250)
    Drive.turn(-90)
    Drive.straight(540)
    Drive.turn(-45)
    Arm.reset()
    Drive.straight(200)
    Missions.mission10()
    Drive.back(250)
    Drive.turn(90)
    Missions.mission5()
    Drive.straight(875, speed=400)
    Drive.turn(45)
    Missions.mission13()
    Drive.back(250, speed=200)
    Drive.curve(-90, -100, then=Stop.COAST_SMART)
    Drive.back(200)
    Drive.straight(500)

def MovementC():
    Arm.turn(25, 90, mode=3)
    Drive.curve(25, 90, then=Stop.COAST_SMART)
    '''
    Drive.straight(25)
    Drive.turn(90)
    Drive.straight(300)
    '''
    Drive.straight(275, then=Stop.COAST_SMART)
    Drive.straight(500, speed=250, then=Stop.COAST_SMART)
    Drive.curve(50, -25, then=Stop.COAST_SMART)
    Drive.curve(50, 25)
    Drive.back(400)
    Drive.turn(-90)
    Missions.mission6()
    Drive.back(200)
    Arm.up()
    Drive.turn(45)
    Drive.back(200, then=Stop.COAST_SMART)
    Drive.back_square()
    Drive.turn(90)
    Missions.mission15()
    Drive.curve(300, 90)
    Missions.mission8()
    '''
    Drive.back(500)
    Drive.turn(-45)
    Drive.back(200)
    '''
    Drive.curve(-600, 55)
    Arm.up()

def MovementD():
    Drive.straight(500)
    Drive.back(500)
