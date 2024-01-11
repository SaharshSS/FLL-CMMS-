from pybricks import version
from pybricks.parameters import Color, Button, Port, Direction, Motor, UltrasonicSensor, ColorSensor, Stop
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

drive = DriveBase(left_motor, right_motor, wheel_diameter=89.231, axle_track=100)

ColorSensor = ColorSensor(Port.C)

Dist = UltrasonicSensor(Port.E)

MovementMode = [0, 0, 0, 0]

adaptive = [100, 50, 30, 50]
fast = [100, 100, 100, 100]
acurite = [50, 50, 30, 25]
test = [10, 10, 10, 10]

#Settings, change these vairables

Commands = [
    "Test",
    "Done"
]

MovementMode = adaptive #Fast, acurite, test and adaptive

def Main():
    Setup()
    Move()
    hub.system.shutdown()

def Setup():
    hub.light.animate([Color.RED * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)
    hub.system.set_stop_button(Button.BLUETOOTH)
    status="Loading"
    print(usys.implementation)
    print(usys.version)
    print(hub.system.name())
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
    drive.use_gyro(True)
    drive.settings(MovementMode)
    drive.reset()
    hub.light.blink(Color.RED, 0.5)
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
    status = "Starting"
    actionCount=0
    while (status != "Done"):
        count = count + 2
        movement = Commands[count-1]
        action = Commands[count]
        print("Movement: " + str(movement))
        print("Action: " + str(action))
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
                    print(action + " error")
        actionCount = actionCount + 1
        print("Count: " + str(count))
        print("Action Count: " + str(actionCount))

def across(): #Not sure of distance
    drive.straight(400)

if __name__ == '__main__':
    print("Running")
    Main()
