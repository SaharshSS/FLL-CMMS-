from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

drive = DriveBase(left, right, wheel_diameter=56, axle_track=139.7)

drive.use_gyro(True)
drive.settings(straight_acceleration = 750, turn_acceleration = 1000)

defaultSpeed = 650

print("Drive.py loaded")

def straight(distance, then = Stop.HOLD, wait = True, speed = defaultSpeed):
    drive.settings(straight_speed = speed)
    drive.straight(distance, then, wait)

def stop():
    drive.stop()

def curve(radius, angle, then = Stop.HOLD, wait = True, speed = defaultSpeed):
    drive.settings(straight_speed = speed)
    drive.settings(turn_rate = speed)
    drive.curve(radius, angle, then, wait)

def turn(angle, then = Stop.HOLD, wait = True, speed = defaultSpeed):
    drive.settings(turn_rate = speed)
    drive.turn(angle, then, wait)

def back(distance, then = Stop.HOLD, wait = True, speed = defaultSpeed):
    drive.settings(straight_speed = speed)
    straight(-distance, then, wait, speed)

def back_square():
    back(250, then=Stop.COAST, speed = 125)
    wait(1500)
