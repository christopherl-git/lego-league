#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait

# Initialize the EV3 brick
ev3 = EV3Brick()

# Beep to indicate the program has started
ev3.speaker.beep()

# Print a message to the console
print("Hello, World! Team 69255 is ready!")

# Display a message on the EV3 screen
ev3.speaker.say("Hello World")

# Beep twice to indicate program completion
ev3.speaker.beep(1000, 100)
ev3.speaker.beep(1000, 100)

print("Program complete!")
