from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor
from pybricks.tools import wait
import Arm, Console, Color

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

left.control.target_tolerances(360, 5)
right.control.target_tolerances(360, 5) 

drive = DriveBase(left, right, wheel_diameter=56.34, axle_track=139.7)

drive.use_gyro(True)
drive.settings(straight_speed = 750, straight_acceleration = 750, turn_rate = 750, turn_acceleration = 1000)

print("Tasks.py loaded")

def NavA():
  drive.turn(-10)
  drive.straight(600)
  drive.turn(105)
  drive.straight(250)
  drive.turn(50)
  #task13
  drive.turn(-140)
  drive.straight(300)
  #sonar discovery
  drive.turn(-90)
  drive.straight(250)
  drive.turn(45)
  drive.straight(600)
  drive.turn(-70)
  drive.straight(800)

def NavB():
  drive.turn(50)
  drive.straight(450)
  drive.turn(-50)
  #Raise the mast
  drive.turn(90)
  drive.back(100)
  drive.turn(-90)
  drive.straight(200)
  drive.turn(-90)
  drive.straight(300)
  #Coral reef
  drive.turn(90)
  #Task 3 shark
  drive.turn(70)
  drive.straight(300)
  #Task 3
  drive.turn(110)
  drive.straight(700)
def NavC():
  drive.tun(-90)
  drive.straight(200)
  #Coral nurserry
  drive.turn(135)
  drive.straight(250)
  drive.turn(-90)
  #task 9 1
  drive.straight(-400)
def NavD():
  drive.turn(-10)
  drive.straight(550)
  drive.turn(-80)
  drive.straight(400)
  drive.turn(-135)
  #Task 9 2, Might not need to remove comment
  drive.turn(180)
  drive.straight(100)
  #Task 14
  drive.straight(-200)
  drive.turn(45)
  drive.straight(100)
  drive.turn(45)
  #Task 10
