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
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=89.231, axle_track=100)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)


# Set a meter stick on the floor and make sure that the robot travels 10 cm.
drive_base.straight(1000)

