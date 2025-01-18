from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
from pybricks import version
import Arm, Missions, Math, Timer, Navigation, Display, Drive, Battery

hub = PrimeHub()

def pushups():
    Drive.straight(0) #Add gyro stabilization
    for i in range(99):
        Display.display(i)
        Arm.turnArm(0, -90, 2, 1000+(i*50))
        wait(500-(i*5))
        Arm.turnArm(-90, -90, 0, 1000+(i*50))
        wait(500-(i*5))
        hub.speaker.beep()

motionList = [Navigation.acrossL, Navigation.acrossR, Navigation.MovementA, Navigation.MovementB, Navigation.MovementC, Navigation.MovementD, Missions.mission1, Missions.mission2, Missions.mission3, Missions.mission4, Missions.mission5, Missions.mission6, Missions.mission7, Missions.mission8, Missions.mission9, Missions.mission10, Missions.mission11, Missions.mission12, Missions.mission13, Missions.mission14, Missions.mission15, pushups] #Missions for testing only
letterList = ["L", "R", "A", "B", "C", "D"]

def setup():
    Timer.reset()
    hub.speaker.beep()
    hub.system.set_stop_button(Button.BLUETOOTH)
    Arm.resetArm()
    Arm.disableArm()
    while not hub.imu.ready():
        wait(1)
    hub.speaker.beep()
    print("Hub name:", hub.system.name())
    print("Hub version:", version)
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
                Display.display(menuList[index])
            if Button.RIGHT in pressed:
                hub.speaker.beep()
                index = index + 1
                index = Math.constrain(index, 0, len(menuList)-1)
                Display.display(menuList[index])
            if Button.CENTER in pressed:
                hub.speaker.beep()
                print("Running:" + str(menuList[index]))
                Display.display(menuList[index])
                Timer.startMission()
                motionList[index]()
                Drive.stop()
                Arm.disableArm()
                print("Mission time:", str(Timer.mTime()) + ", Total time:", str(Timer.time()))
                voltage = Battery.voltage()
                print("Battery voltage:", str(voltage) + ", Battery percentage:", str(Battery.percentage(voltage)))
        else:
            displayOn = Display.display(menuList[index], displayOn)
        wait(100)
setup()
main()
