from pybricks import version
from micropython import const, opt_level, mem_info, qstr_info, stack_use
from pybricks.parameters import Color, Button, Port, Direction, Motor, UltrasonicSensor, ColorSensor, Stop, Side, Icon
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import multitask, run_task, wait
from math import sin, pi
import usys

#Don't change these because don't

hub = PrimeHub()

ArmA = Motor(Port.D)
ArmB = Motor(Port.F)

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

drive = DriveBase(left_motor, right_motor, wheel_diameter=90, axle_track=100) #Double check wheel_diameter!!

ColorSensor = ColorSensor(Port.C)

Dist = UltrasonicSensor(Port.E)

MovementMode = [0, 0, 0, 0]
# Meaning of each variable:
# MovementMode = [straight_speed, straight_acceleration, turn_rate, turn_acceleration]

# Possible Movement Modes
adaptive = [100, 50, 30, 50]
fast = [100, 100, 100, 100]
accurate = [50, 50, 30, 25]
test = [10, 10, 10, 10]

#Settings, change these variables

Commands = [
    "Test",
    "Done"
]

MovementMode = adaptive # fast, accurate, test and adaptive

def Main():
    Setup()
    Move()
    hub.system.shutdown()

def Setup():
    hub.light.blink(Color.RED, 0.5)
    hub.system.set_stop_button(Button.BLUETOOTH)
    status="Loading"
    print(usys.implementation)
    print(usys.version)
    print(version)
    print(hub.system.name())
    mem_info(True)
    qstr_info(True)
    if (hub.system.reset_reason() == 2):
        print("Rebooting from error")
    print("Booting") 
    print(" ________________________________")   
    print("|Information       |Value/t/t|")
    print("|------------------+-------------|")
    print("|Battery voltage   |" + str(hub.battery.voltage()) + " mV/t|")
    print("|Battery current   |" + str(hub.battery.current()) + " mA/t|")
    print("|BLE version       |" + hub.ble.version() + " /t|")
    print("|BLE power         |" + str(hub.ble.signal_strength())) + "Dpm/t|"
    print("|Controller Limits |" + str(hub.control.limits())) + "/t|"
    print("|Controller Pid    |" + str(hub.control.pid()))+ "/t|"
    print("'--------------------------------'")
    if hub.charger.connected():
        if (hub.charger.status() == 1):
            print("Charging")
        elif (hub.charger.status() == 2):
            print("Battery full")
        else:
            print("Error!")
    Dist.lights.on(1, 1, 0, 0)
    ColorSensor.lights.on([100, 0, 0])
    hub.light.animate([Color.RED * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)
    drive.use_gyro(True)
    drive.settings(MovementMode)
    drive.reset()
    hub.speaker.volume(100)
    hub.imu.reset_heading()
    hub.speaker.beep()
    hub.speaker.beep(600)
    hub.speaker.beep(700, 200)

def turnArm(Arm1, Arm2, Mode = 2, Speed = 500):
    print("Turning arm " + str(Arm1) + ", " + str(Arm2) + ", mode " + str(Mode) + ", Speed " + str(Speed))
    if (Mode == 2):
        multitask(ArmA.run_target(Speed, Arm1), ArmB.run_target(Speed, Arm2))
    elif (Mode == 1):
        ArmA.run_target(Speed, Arm1)
        ArmB.run_target(Speed, Arm2)
    else:
        ArmB.run_target(Speed, Arm2)
        ArmA.run_target(Speed, Arm1)

def TrackLine(Distance):
    print("Tracking line to " + str(Distance))
    NewDirection=0
    NewDistance=0
    while (Distance > NewDistance):
        if (ColorSensor.color() == "White"):
            if (NewDirection == 1):
                NewDirection = 0
                while (ColorSensor.color() != "White"):
                    drive.curve(20, 1, Stop.COAST)
        else:
            NewDirection = 1
            if (ColorSensor.color() == "White"):
                if (NewDirection == 1):
                    NewDirection = 0
                    while (ColorSensor.color() != "White"):
                        drive.curve(-20, 1, Stop.COAST)
        drive.straight(1)
        NewDistance=NewDistance+0.5

def TrackLine1(Distance, Direction = True):
    print("Tracking line for " + str(Distance))
    NewDirection = 0
    NewDistance = 0
    if (Direction):
        while(NewDistance < Distance):
            if (ColorSensor.color() == "White"):
                drive.curve(-20, 1, Stop.COAST)
            else:
                drive.curve(20, 1, Stop.COAST)
            NewDistance = NewDistance + 1
    else:
        while(NewDistance < Distance):
            if (ColorSensor.color() == "White"):
                drive.curve(20, 1, Stop.COAST)
            else:
                drive.curve(-20, 1, Stop.COAST)
            NewDistance = NewDistance + 1

def TestAll():
    print("Please Press Y to continue")
    if hub.keyboard.poll(0):
        # Read the key and print it.
        TestVar = hub.stdin.read(1)
        TestVar = str(TestVar)
    if (TestVar == "Y"):
        print("Success")
    else:
        print("Error")
    print("Testing arm")
    turnArm(0, 0, 2, 1000)
    if (ArmA.angle() == 0 and ArmB.angle() == 0):
        print("Success")
    else:
        print("Error")

def Move(count = 0):
    status = "Working"
    actionCount= 0
    count = 0
    while (status != "Done"):
        count = count + 2
        movement = Commands[count-1]
        action = Commands[count]
        print("Movement: " + str(movement))
        print("Action: " + str(action))
        hub.display.number(actionCount);
        if (action == "Forward"): #Two input functions EX: Forward, Turn
            drive.straight(movement)
        elif (action == "Turn"):
            drive.curve(movement, 1)
        elif (action == "Track Line"):
            TrackLine(movement)
        else:
            count = count - 1 #Single input functions EX: Across
            if (action == "Across"):
                across()
            elif (action == "Done"):
                print("Program ended")
                wait(100)
            else: #Tri input functions EX: Arm
                count = count + 2
                movement2 = Commands[count-2]
                if (action == "Arm"):
                    turnArm(movement, movement2)
                else:
                    status = "Error!"
                    print(action + " error. Not supported")
        actionCount = actionCount + 1
        print("Count: " + str(count))
        print("Action Count: " + str(actionCount))
        pressed = []
        while not any(pressed):
            pressed = hub.button.pressed()
        if (Button.LEFT in pressed):
            hub.display.icon(Icon.ARROW_LEFT)
            count = count - 1
        elif (Button.RIGHT in pressed):
            hub.display.icon(Icon.ARROW_RIGHT)
        wait(1000)
        hub.speaker.beep()
def across(): #Not sure of distance
    drive.straight(400)
    drive.curve(15, 45)

if __name__ == '__main__':
    print("Running")
    Main()
#---------------------------------------------------------------------------------------------------------------------------------
#Selector Algorithm for Multiple Runs
#This is our menu as on Pybricks there is no option for having 2 codes on 1 hub at the same time
menu_options = ("1", "2", "3", "4", "5", "6", "7", "8", "9", ) #forward, left, right, back, exit
menu_index = 0
num_options = len(menu_options)
hub = PrimeHub()

# Clear terminal
print("\x1b[H\x1b[2J", end="")

def do_menu(hub):
    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
    global menu_index
    hub.system.set_stop_button(Button.BLUETOOTH)
    while True:
        hub.display.char(menu_options[menu_index])
        # Wait for any button.
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)
        # and then wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)
  
        # Now check which button was pressed.
        if Button.CENTER in pressed:
            # Center button, this is the selection button, so we can exit the
            # selection loop
            break
        elif Button.LEFT in pressed:
            # Left button, so decrement menu menu_index.
            menu_index -= 1
            if (menu_index < 0): #roll over!
                menu_index = num_options - 1
        elif Button.RIGHT in pressed:
            # Right button, so increment menu menu_index.
            menu_index += 1
            if (menu_index >= num_options):
                menu_index = 0
    
    # Now we want to use the Center button as the stop button again.
    hub.system.set_stop_button(Button.CENTER)
    selected = menu_options[menu_index]
    return selected

selected = ""
while True:
    selected = do_menu(hub)
    if selected == "1"
        #Run 1
    elif selected == "2"
        #Run 2
    elif selected == "3"
        #Run 3
    elif selected == "4"
        #Run 4
    elif selected == "5"
        #Run 5
    elif selected == "6"
        #Run 6
    elif selected == "7"
        #Run 7
    elif selected == "8"
        #Run 8
    elif selected == "9"
        #Run 9
