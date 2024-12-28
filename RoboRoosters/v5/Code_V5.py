from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
import Arm, Missions, Math, Timer, Navigation, Display, Battery

hub = PrimeHub()

motionList = [Navigation.acrossL, Navigation.acrossR, Navigation.MovementA, Navigation.MovementB, Navigation.MovementC, Navigation.movementD, Missions.mission1, Missions.mission2, Missions.mission3, Missions.mission4, Missions.mission5, Missions.mission6, Missions.mission7, Missions.mission8, Missions.mission9, Missions.mission10, Missions.mission11, Missions.mission12, Missions.mission13, Missions.mission14, Missions.mission15] #Missions for testing only
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
    print("Hub version:", version)
    print("Battery voltage:", voltage + ", Battery percentage:", Battery.percentage(voltage))

def main():
    index = 2
    menuList = letterList+range(len(motionList)-len(letterList))
    print("Generated list:", menuList)
    while True:
        Display.display(menuList[index])
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed: 
            index = index - 1
        if Button.RIGHT in pressed:
            index = index + 1
        if Button.CENTER in pressed:
            print("Running:", motionList[index].__name__)
            Display.display(menuList[index])
            Timer.startMission()
            motionList[index]()
            print("Mission time:", Timer.mTime() + ", Total time:", Timer.time())
            voltage = Battery.voltage()
            print("Battery voltage:", voltage + ", Battery percentage:", Battery.percentage(voltage))
        index = Math.constrain(index, 0, len(menuList)-1)   

setup()
main()
