from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
import Arm, Console, Tasks, Math

hub = PrimeHub()

TaskList = [Tasks.task1, Tasks.task2, Tasks.task3, Tasks.task4, Tasks.task5, Tasks.task6, Tasks.task7, Tasks.task8, Tasks.task9, Tasks.task10, Tasks.task11, Tasks.task12, Tasks.task13, Tasks.task14, Tasks.task15]

def setup():
    hub.speaker.beep()
    hub.system.set_stop_button(Button.BLUETOOTH)
    Arm.resetArm()
    while not hub.imu.ready():
        wait(1)
    hub.imu.reset_heading(0)
    hub.speaker.beep()
    
def main():
    index = 0
    d = 0
    while True:
        b = hub.buttons.pressed()
        if Button.CENTER in b:
            if index == 0:
                b = hub.buttons.pressed()
                while not Button.RIGHT in b and not Button.LEFT in b:
                    b = hub.buttons.pressed
                    if d < 2:
                        hub.display.char("A")
                    else:
                        hub.display.off()
                if Button.RIGHT in b:
                    Tasks.across(1)
                else:
                    Tasks.across()
            else:
                Console.Run(index, TaskList[index-1])
                index += 1
        if Button.LEFT in b:
            index -= 1
            hub.speaker.beep()
            d = 1
        if Button.RIGHT in b:
            index += 1
            d = 1
            hub.speaker.beep()
        index = Math.constrain(index, 0, len(TaskList)-1)
        if d < 2:
            if index == 0:
                hub.display.char("A")
            else:
                Console.dispNumber(index)
            d += 1
        else: 
            hub.display.off()
            d = 0
        wait(100)
setup()
main()
