"""
NOTE, THIS IS THE ONE THAT IS IN THE "mu_code" DIRECTORY

Micro:Bit->TinyBitRobot: Movement Module

This was made in order to combat the "trial-and-error" approach to rotating the robot, I don't have an encoder but the closest
thing I got is the compass feature of the microbit which can recognise direction. Note, momentum of the robot itself can cause it to still overshoot the turn, different surfaces yield different results
The motor encoder can convert the electrical signals to data that described the rotatary shaft's speed and angle (I don't have that)

Now, this movment only supports turning of either:
    - SpinLeft/SpinRight (where it spins across the centre of the robot)
    - Left/Right (Where one wheel does not turn and the robot pivots about the wheel rather than its own origin)

The approach, rather than the very vague paramters of its intensity (1-255) provided by the tinybit robot package and the time for it to do the turn,
I will approach it as:
    1) The Degrees you want it to turn (Can only be in integers)
    2) DC motor power, ranging from 0-255 (same as what yahboom provides).
    * Note: There can not be a parameter for the exact time for it to turn as there is no direct proportionality between the power applied to the DC motors and the rate of which it turns that I can exploit (it's not accurate)
-- This will allow much easier and perhaps even more accurate turning
"""


from microbit import *
import tinybit # Sourced from Yahboom's site, is part of their firmware you download


def __spinDirection(angle, direction, power): # May include the time_in_seconds paramter
    if power < 0 or power > 255:
        raise ValueError("Power can only be within the range of 0 to 255 inclusive")
        return
        # Range Check
    elif int(power) != power or int(angle) != angle:
        raise TypeError("Power and Angle both have to be integers (whole numbers)")
        return
        # Type Check



    # time_in_ms = time_in_seconds * 1000
    current_angle = compass.heading()

    if direction == "right":
        goal_angle = (current_angle + angle) % 360

    elif direction == "left":
        goal_angle = (current_angle - angle) % 360 # Remember, mod always gives a positive number

    # Find co-terminal angles that are greater than 360 to be limited to what the compass supports as an integer

    goal_upper_bound = (goal_angle + 10) % 360
    goal_lower_bound = (goal_angle - 10) % 360
    # Use value ranges due to the imprecise movement of DC motors

    while current_angle < goal_lower_bound or current_angle > goal_upper_bound:
        if direction == "left":
            tinybit.car_spinleft(power)

        elif direction == "right":
            tinybit.car_spinright(power)

        sleep(1)
        tinybit.car_stop()
        current_angle = compass.heading()


def spinLeft(angle, power):
    __spinDirection(angle, "left", power)


def spinRight(angle, power):
    __spinDirection(angle, "right", power)


compass.calibrate() # Before the TinyBit robot can start, its compass needs to be callibrated to recognise rotation
