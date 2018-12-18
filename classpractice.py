'''
    On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 
 
    For some of these problems you will need to create a class; for others, you will need to use a library. 
    You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''
 
 
 
 
 
''' 1.
    Create a class, Point, that keeps track of two properties: x and y
    When a point is created, values for x and y should be provided.
 
    The methods for this class are as follows:
    rotate90: rotate the point 90° about the origin
    rotate180: rotate the point 180° about the origin
    rotaten90: rotate -90° about the origin
    translate: given 2 values, translate the point by the given amount.
    flip_horizontally: flip the point on the x-axis
    flip_vertically: flip the point on the y-axis
'''

 
 
 
 
''' 2.
    Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
    When a Bicycle is created, cadence, gear, and speed are accepted as arguments.
 
    The methods for this class are as follows:
    set_gear: given a value, set the gear to that value
    set_cadence: given a value, set the cadence to that value
    apply_brake: given a value, decrease the speed of the bike by that value
    speed_up: given a value, increase the speed of the bike by that value
'''
class Bicycle:
    def __init__(self, cadence, gear, speed):
        self.cadence = cadence
        self.gear = gear
        self.speed = speed

    def set_gear(self, gear):
        self.gear = gear
        info = "Gear is", self.gear
        return info

    def set_cadence(self, cadence):
        self.cadence = cadence
        info = "Cadence is ", self.cadence
        return info

    def apply_brake(self, brake):
        self.speed -= brake
        info = "Speed after brake is", self.speed
        return info

    def speed_up(self, acceleration):
        self.speed += acceleration
        info = "Speed after acceleration is", self.speed
        return info


 
 
 
 
''' 3.
    Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
    These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.
 
    The methods for the student class are as follows:
    study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
    sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
    class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
    take_test: Given a value (to adjust hours), this increases stress. 
    submit_paper: this decreases stress.
    eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
    sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
    new_day: resets the hours in a day.
 
    You may not let a student do more than 24 hours worth of activities in a given day. 
'''
 
 
 
 
 
''' 4. 
    Use numpy to create an array of numbers going from 20 to 100 by increments of .25
    Then, multiply all the values in the array by 4. 
    Then. find the sum of all the values.
'''
import numpy as np

list = np.arrange(20,100.1,0.25)

list = list*4

total = np.sum(list)

https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.sum.html
https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.sum.html
https://docs.scipy.org/doc/numpy-1.15.0/user/quickstart.html
 

 
''' 5.
    Use turtle to draw a star.
'''
 
 
 
 
 
''' 6.
    Use SymPy to determine the area of a triangle given points a, b and c.
'''
from sympy.geometry import triangle
x = (0,0)
y = (0,6)
z = (3,6)
tri = Triangle(z, y, z)
area = tri.area()

 
 
 
 
''' 7. 
    Use VPython to build a 3D snowman.
'''
 
 
 
 
''' Sources:
    https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
'''