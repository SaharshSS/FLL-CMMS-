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

def Main():
    Setup()
    Move()
    hub.system.shutdown()

def setup():
    print("Version: " + str(version))
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

menu = 0

def main():
    while menu > len(tasks):
        hub.display.char(int(menu))
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
        if Button.CENTER in pressed:
            break
        if Button.LEFT in pressed or Button.DOWN in pressed:
            if menu > 0:
                menu -= 1
        elif BUtton.RIGHT in pressed or Button.UP in pressed:
            if menu < len(tasks):
                menu += 1
    tasks[menu]()
