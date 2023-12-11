from pybricks import version
from pybricks.parameters import Color, Button, Port, Direction, Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import multitask, run_task, wait
from math import sin, pi

Commands = [
    "Test",
    "Done"
]
Status = "Starting"

def Setup():
    hub = PrimeHub()
    hub.light.animate([Color.RED * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)
    hub.system.set_stop_button(Button.BLUETOOTH)
    status="Loading"
    print(usys.implementation)
    print(usys.version)
    print(system.name())
    if (system.reset_reason() == 2):
        print("Rebooting from error")
    print("Booting")
    print("Battery voltage: " + str(battery.voltage()) + " mV")
    print("Battery current: " + str(battery.current()) + " mA")
    print("BLE version: " + ble.version())
    print("BLE dBm: " + str(ble.signal_strength()))
    if charger.connected():
        if (charger.status() == 1):
            print("Charging")
        elif (charger.status() == 2):
            print("Battery full")
        else:
            print("Error!")
    Dist = UltrasonicSensor(Port.E)
    lights.on(1, 1, 0, 0)
    ArmA = Motor(Port.D)
    ArmB = Motor(Port.F)
    ColorSense = ColorSensor(Port.C)
    ColorSense.lights.on([100, 0, 0])
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.B)
    drive = DriveBase(left_motor, right_motor, wheel_diameter=89.231, axle_track=100)
    drive.use_gyro(True)
    light.blink(color.red, 0.5)
    speaker.volume(100)
    imu.reset_heading()
    speaker.beep()
    speaker.beep(600)
    speaker.beep(700, 200)

def turnArm(Arm1, Arm2, Mode = 2, Speed = 500):
    if (Mode == 2):
        multitask(ArmA.run_target(Speed, Arm1), ArmB.run_target(Speed, Arm2))
    elif (Mode == 1):
        ArmA.run_target(Speed, Arm1)
        ArmB.run_target(Speed, Arm2)
    else:
        ArmB.run_target(Speed, Arm2)
        ArmA.run_target(Speed, Arm1)

def TrackLine(Distance):
    NewDirection=0
    NewDistance=0
    while (Distance > NewDistance):
        if (ColorSense.color() == "White"):
            if (NewDirection == 1):
                NewDirection = 0
                while (ColorSense.color() != "White"):
                    drive.curve(20, 1, Stop.COAST)
        else:
            NewDirection = 1
            if (ColorSense.color() == "White"):
                if (NewDirection == 1):
                    NewDirection = 0
                    while (ColorSense.color() != "White"):
                        drive.curve(-20, 1, Stop.COAST)
        drive.straight(1)
        NewDistance=NewDistance+0.5

def TrackLine1(Distance, Direction = True):
    NewDirection = 0
    NewDistance = 0
    while (Distance>NewDistance):
        #Code later Kevin annoying

def TestAll():
    TestVar = int(input("Testing serial connection, please press one"))
    if (TestVar == 1):
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
    actionCount=0
    while (status != "Done"):
        count = count + 2
        movement = Commands[count-1]
        action = Commands[count]
        if (action == "Test"):
            TestAll()
            count = count - 1
        elif (action == "Across"):
            across()
            count = count -1
        elif (action == "Done"):
            print("Program ended, shutting down")
            wait(100)
            hub.system.shutdown()
        else:
            status = "Error!"
            print(action + "not Supported")
        actionCount = actionCount + 1
        print("Count: " + str(count))
        print("Action Count: " + str(actionCount))

def across(): #Not sure of distance
    straight(400)
