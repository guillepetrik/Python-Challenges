#Polar Coordinates Challenge

# Importing the cmath module to perform complex number operations
import cmath

# Prompting the user to input a complex number and stripping any leading/trailing spaces
c = complex(input().strip())

# Computing the polar coordinates of the complex number using the cmath.polar() function
# The result is a tuple containing the magnitude (radius) and phase (angle) of the complex number
sol = cmath.polar(c)

# Printing the magnitude (radius) and phase (angle) of the complex number
print(sol[0])
print(sol[1])
