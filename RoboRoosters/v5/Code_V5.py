from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
import Arm, Missions, Math, Timer, Navigation, Display, Drive, Battery, usys

hub = PrimeHub()

def pushups():
    Drive.straight(0) #Add gyro stabilization
    for i in range(99):
        Display.number(i)
        Arm.turn(0, -90, 2, 1000+(i*50))
        wait(500-(i*5))
        Arm.turn(-90, -90, 0, 1000+(i*50))
        wait(500-(i*5))
        hub.speaker.beep()

motionList = [Navigation.acrossL, Navigation.acrossR, Navigation.MovementA, Navigation.MovementB, Navigation.MovementC, Navigation.MovementD, Missions.mission1, Missions.mission2, Missions.mission3, Missions.mission4, Missions.mission5, Missions.mission6, Missions.mission7, Missions.mission8, Missions.mission9, Missions.mission10, Missions.mission11, Missions.mission12, Missions.mission13, Missions.mission14, Missions.mission15, pushups] #Missions for testing only
letterList = ["L", "R", "A", "B", "C", "D"]

def setup():
    Timer.reset()
    hub.speaker.volume(100)
    hub.speaker.beep()
    hub.system.set_stop_button(Button.BLUETOOTH)
    while not hub.imu.ready():
        wait(1)
    hub.speaker.beep()
    print("Hub name:", hub.system.name())
    print("Hub version:", usys.version)
    print("Hub implementation:", usys.implementation)
    voltage = Battery.voltage()
    print("Battery voltage:", str(voltage) + ", Battery percentage:", str(Battery.percentage(voltage)))

def main():
    index = 2
    displayOn = False
    menuList = letterList
    menuList.extend(range(1, len(motionList)-len(letterList)+1))
    print("Generated list:", menuList)
    while True:
        pressed = hub.buttons.pressed()
        if pressed:
            if Button.LEFT in pressed:
                hub.speaker.beep() 
                index = index - 1
                index = Math.constrain(index, 0, 100)
                Display.number(menuList[index])
            if Button.RIGHT in pressed:
                hub.speaker.beep()
                index = index + 1
                index = Math.constrain(index, 0, len(menuList)-1)
                Display.number(menuList[index])
            if Button.CENTER in pressed:
                hub.speaker.beep()
                print("Running:" + str(menuList[index]))
                Display.number(menuList[index])
                Timer.startMission()
                motionList[index]()
                Drive.stop()
                Arm.disable()
                print("Mission time:", str(Math.convert_millis(Timer.mTime())) + ", Total time:", str(Math.convert_millis(Timer.time())))
                voltage = Battery.voltage()
                print("Battery voltage:", str(voltage) + " mv, Battery percentage:", str(Battery.percentage(voltage)))
        else:
            displayOn = Display.number(menuList[index], displayOn)
        wait(100)
setup()
main()
