import math
import random

temp = float(input("Fahrenheit: "))
vel = float(input("Wind Velocity: "))

# temp = float (temp)
# float (vel)

w = 35.74 + 0.6215*(temp) + (0.4275*(temp) - 35.75)*(vel)**0.16

print ("Wind chill:", w)