from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.parameters import Color, Button, Port, Direction, Motor, UltrasonicSensor, ColorSensor, Stop, Side, Icon
from pybricks.tools import multitask, run_task, wait

hub = PrimeHub()

armBase = Motor(Port.D)
armMid = Motor(Port.F)

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

drive = DriveBase(left, right, wheel_diameter=90, axle_track=100)

color = ColorSensor(Port.C)

distance = UltrasonicSensor(Port.E)

def setup():
    drive.reset()
    drive.use_gyro(True)
    drive.settings(100, 50, 30, 50) #[straight_speed, straight_acceleration, turn_rate, turn_acceleration]
    hub.imu.reset_heading()
    hub.speaker.volume(50)
    hub.speaker.beep(500)

def turnArm(angle2, angle2, mode = 0, speed = 500):
    if not mode:
        multitask(armBase.run_target(speed, angle2), armMid.run_target(speed, angle2))
    elif mode == 1:
        armBase.run_target(speed, angle2)
        armMid.run_target(speed, angle2)
    else:
        armMid.run_target(speed, angle2)
        armBase.run_target(speed, angle2)

def across():
    drive.straight(200)

tasks = [across()]
inputs = [100]
inputCount =  0
menu = 0

def TrackLine(Distance):
    NewDirection = 0
    NewDistance = 0
    while NewDistance < Distance:
        if ColorSensor.color() == "White":
            NewDirection = 1 if NewDirection == 0 else 0
            while ColorSensor.color() != "White":
                drive.curve(20 * NewDirection, 1, Stop.COAST)
            drive.straight(1)
            NewDistance += 0.5

def TrackLine1(Distance, Direction=True):
    curve_direction = 20 if Direction else -20
    while NewDistance < Distance:
        if ColorSensor.color() == "White":
            drive.curve(-curve_direction, 1, Stop.COAST)
        else:
            drive.curve(curve_direction, 1, Stop.COAST)
        NewDistance += 1

def main():
    setup()
    global menu, inputCount
    while menu < len(tasks):
        hub.display.char(menu)
        pressed = hub.buttons.get_pressed()
        if Button.CENTER in pressed:
            break
        if Button.LEFT in pressed or Button.DOWN in pressed:
            if menu > 0:
                menu -= 1
        else:
            if menu < len(tasks) - 1:
                menu += 1
        try:
            tasks[menu]()
        except TypeError:
            input_value = input("Enter input: ")
            tasks[menu](input_value)
            inputCount += 1
