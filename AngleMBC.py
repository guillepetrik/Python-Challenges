# Find Angle MBC

import math  # Import the math module to access mathematical functions

# Prompt for user input to get the values of AB and BC
AB = int(input())
BC = int(input())

# Calculate the angle using trigonometric functions and convert it to degrees
angle = math.degrees(math.atan(AB/BC))

# Print the rounded angle value followed by the degree symbol
print(round(angle), chr(176), sep="")
