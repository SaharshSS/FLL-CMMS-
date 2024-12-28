import Drive, Arm, Missions

def acrossL():
    drive.curve(200, -90)
    wait(100)
    drive.straight(1200)
    drive.curve(200, -65)

def acrossR():
    drive.curve(200, 90)
    wait(100)
    drive.straight(1200)
    drive.curve(200, 65)

def MovementA():
    Drive.turn(-90)
    Drive.straight(100)
    Missions.mission8()
    Arm.armUp()
    Drive.turn(-45) #map heading 135
    Drive.straight(420) #1 krill
    Drive.back(65)
    Drive.turn(75) #map heading 60
    Drive.straight(375)
    Drive.turn(-345) #map heading 45, 3 krill
    Missions.mission13()
    Drive.turn(-180)
    Drive.straight(150)
    Missions.mission11() #Empty now, fill later
    Drive.straight(400)
    Arm.armUp()
    Drive.turn(90)
    Drive.back(100)
    Missions.mission10()
    Drive.turn(-90)
    Drive.back(100)
    Drive.turn(90)
    Missions.mission14()
    Drive.turn(-90)
    Drive.straight(350)
    Drive.turn(-60)
    Drive.straight(700, speed = 250)

def MovementB():
    Drive.turn(20)
    Drive.straight(550)
    Drive.turn(-110)
    Missions.mission1()
    Drive.turn(90)
    Drive.straight(50)
    Drive.turn(-90)
    Missions.mission4()
    Drive.turn(45)
    Drive.straight(250)
    Missions.mission2()
    Drive.turn(90)
    Drive.straight(125)
    Drive.turn(45)
    Missions.mission3()
    Drive.turn(100)
    Drive.straight(900)

def MovementC():
    drive.turn(75)
    drive.straight(450)
    drive.turn(-75)
    Missions.mission6() #Idk Mission 6 would be blank I guess
    Missions.mission7()
    drive.turn(-180)
    drive.straight(250)
    drive.turn(-90)
    Missions.mission15()

def MovementD():
    drive.turn(-52) #Rly precise measurement for dis one
    drive.straight(110)
    drive.turn(142)
    drive.straight(825)
    drive.turn(-45)
    Missions.mission(12)
