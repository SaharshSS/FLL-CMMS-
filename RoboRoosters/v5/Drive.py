from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

drive = DriveBase(left, right, wheel_diameter=62.4, axle_track=127)

drive.use_gyro(True)
drive.settings(straight_acceleration = 750, turn_acceleration = 750)

_DEFAULT_SPEED = 750

def straight(distance, then = Stop.HOLD, wait = True, speed = _DEFAULT_SPEED):
    while not drive.done: 
        wait(10)
    drive.settings(straight_speed = speed)
    drive.straight(distance, then, wait)

def stop():
    while not drive.done:
        wait(10)
    drive.stop()

def curve(radius, angle, then = Stop.HOLD, wait = True, speed = _DEFAULT_SPEED):
    while not drive.done: 
        wait(10)
    drive.settings(straight_speed = speed)
    drive.settings(turn_rate = speed)
    drive.curve(radius, angle, then, wait)

def turn(angle, then = Stop.HOLD, wait = True, speed = _DEFAULT_SPEED):
    while not drive.done: 
        wait(10)
    drive.settings(turn_rate = speed)
    drive.turn(angle, then, wait)

def back(distance, then = Stop.HOLD, wait = True, speed = _DEFAULT_SPEED):
    while not drive.done: 
        wait(10)
    drive.settings(straight_speed = speed)
    straight(-distance, then, wait, speed)

def back_square():
    while not drive.done: 
        wait(10)
    drive.settings(straight_speed = 125)
    back(125, then=Stop.COAST)

def front_square():
    while not drive.done: 
        wait(10)
    drive.settings(straight_speed = 125)
    straight(125, then=Stop.COAST)

print("Drive.py loaded")
