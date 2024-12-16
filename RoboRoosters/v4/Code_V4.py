from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
import Arm, Console, Tasks, Math, Timer, Color

hub = PrimeHub()

TaskList = [Tasks.acrossl, Tasks.acrossr, Tasks.task1, Tasks.task2, Tasks.task3, Tasks.task4, Tasks.task5, Tasks.task6, Tasks.task7, Tasks.task8, Tasks.task9, Tasks.task10, Tasks.task11, Tasks.task12, Tasks.task13, Tasks.task14, Tasks.task15, Tasks.pushups, Color.getColor]

def setup():
    Timer.reset()
    hub.speaker.beep()
    hub.system.set_stop_button(Button.BLUETOOTH)
    Arm.resetArm()
    Arm.disableArm()
    while not hub.imu.ready():
        wait(1)
    hub.imu.reset_heading(0)
    hub.speaker.beep()
    Console.Stats()
    
def main():
    index = 0
    display = 0
    allerted = 0
    while True:
        buttons = hub.buttons.pressed()
        if Button.CENTER in buttons:
            Console.Run(index, TaskList[index+1])
            index += 1
        if Button.LEFT in buttons:
            index -= 1
            hub.speaker.beep()
            display = 1
        if Button.RIGHT in buttons:
            index += 1
            display = 1
            hub.speaker.beep()
        index = Math.constrain(index, -1, len(TaskList)-2)
        if display < 2:
            Console.dispMenu(index)
            display += 1
        else: 
            hub.display.off()
            display = 0
        wait(100)
        if Timer.time() > 100000 and allerted < 1:
            print("")
            print("20 seconds left!")
            allerted = 1
        if Timer.time() > 150000 and allerted < 2:
            print("")
            print("2:30 minutes is up!")
            if Timer.time() < 150005:
                print("Overtime " + str(Timer.time-150000) + "ms")
            allerted = 2
            for i in range(10):
                hub.speaker.beep()
setup()
main()
