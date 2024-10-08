from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 80mm.
# If you would like to convert studs to mm, go here: http://studs.sariel.pl/
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

# Adds Gyro
drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
drive_base.straight(500)

# Turn around clockwise by 180 degrees.
drive_base.turn(180)

# Drive forward again to get back to the start.
drive_base.straight(500)

# Turn around counterclockwise.
drive_base.turn(-180)

# Make a curve
drive_base.curve(20, 360)
