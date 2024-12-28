from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

left.control.target_tolerances(360, 5)
right.control.target_tolerances(360, 5) 

drive = DriveBase(left, right, wheel_diameter=56.34, axle_track=139.7)

drive.use_gyro(True)
drive.settings(straight_acceleration = 750, turn_acceleration = 1000)

print("Drive.py loaded")

def straight(distance, then = Stop.HOLD, wait = True, speed = 750):
    drive.settings(straight_speed = speed)
    drive.straight(distance, then, wait)

def stop():
    drive.stop()

def curve(radius, andle, then = Stop.HOLD, wait = True, speed = 750):
    drive.settings(straight_speed = speed)
    drive.settings(turn_speed = speed)
    drive.curve(radius, angle, Stop, wait)

def turn(angle, then = Stop.HOLD, wait = True, speed = 750):
    drive.settings(turn_speed = speed)
    drive.turn(angle, then, wait)

def back(distance, then = Stop.HOLD, wait = True, speed = 750):
    straight(-distance, then, wait, speed)
