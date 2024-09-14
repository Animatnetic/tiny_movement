# Tiny Movement

## What is `tiny_movement`?

Movement module for TinyBit Robots by Yahboom[https://category.yahboom.net/]. These robots are controlled by Microbit Microcontrollers, yet you can extend this to whatever MicroBit controlled robot you have by changing up the methods that are responsible for the robot's specific rotation


## How it Works?

This module is meant to add more customization and accuracy to how is your robot rotated. For example, Yahboom's TinyBit robots have rotation functions within their API that only supports a parameter from 0 to 255 which describes the power allocated to the DC motor. This poses an issue when we want to rotate the robot a specific number of degrees. Before, we would have to do a "trial-and-error" approach where we hard-code the the power allocated to the DC motor for rotation and how long do we have the roation be in motion before we stop the motor. This is not only tedious to do, yet is inaccurate as we would have to do a whole other "trial-and-error" approach for when the robot is on a different surface.

Now instead, we use the compass feature of the microbit to get the initial angle that the robot is facing and get the current angle of the robot as it changes, only stopping for once it has reached the desired angle that has been inputted into the parameter. Hence, even if it where to hit a wall, went on a different surface material, etc. It will still continue to rotate until, and only then stop, when it has reached its desired angle.

### Here is a list of functions `Mini Docs`:

#### `tiny_movement.spinLeft(angle, power)`: Spin the robot left, at the centre from its origin, by the following parameter

- angle: The angle to turn the robot (in degrees), can be betwene 0 to 360 or more but it will appear as the co-terminal angles from 0 to 360 degreess : *integer*
- power: The amount of strength allocated to the DC motors for it to turn, between 0 to 255 inclusive **only** : *integer*

#### `tiny_movement.spinRight(angle, power)`: Spin the robot right, at the centre from its origin, by the following parameter

- angle: The angle to turn the robot (in degrees), can be betwene 0 to 360 or more but it will appear as the co-terminal angles from 0 to 360 degreess : *integer*
- power: The amount of strength allocated to the DC motors for it to turn, between 0 to 255 inclusive **only** : *integer*

## What is the Value of this Module?
Under normal circumstances, if you want precision with the movement of DC motors, you would use an `encoder`. The DC motors in the TinyBit robots do *not* come with encoders. Hence, this is a compensation for accuracy that comes with Microbits by default with their compass feature. Encoder's are also harder to use so you can use this module as pre-requisite knowledge to translate the robot's current orientation as digital data and how to manipulate it.


## How to Install and import?
### Install Process:
If you don't already know, you could:
  1. Create a new director
  2. `cd` into that new director
  3. write `git clone [TOB]` into your terminal

### Importing and using the module
1. Before your `TinyBit`, or whatever, robot can use the Module, you need to have this module be written within the Microbit filesystem that controls the robot.
2. Assuming you use **mu editor**, you need to:
    1. Find the python script `tiny_movement.py` from the directory you initially cloned the git repo
    2. Relocate the python script over to `mu_code` folder (this is the folder that houses your root files that the mu_code editor has access to)
    3. Using mu editr, clicking "Files" on the top bar, and drag over the computer files containing `tiny_movement.py` to the `MicroBit` files section within the IDE and wait for it to be copied (Ensure your MicroBit is connected via USB for this step)
    * Note, if you do not use **mu editor** you need to install it, or, if you know what you are doing, you need to somehow have the python script be within the Microbit's Local Peristent file system before your other flashed python code can use it
3. ```py
   import tiny_movement
   ```
   at the top of your python code to use its methods
