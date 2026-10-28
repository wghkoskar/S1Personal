# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    Creates a point in a 2D space.
    """
    def __init__(self, x=0.0, y=0.0):
        """
        Assigns values to the point
        """
        self.x = x
        self.y = y 

    def distance(self):
        """
        Returns the distance between the X and Y coordinates
        """

        return hypot(self.x, self.y)

    def distance_to(self, point2):
        """
        Returns the distance between two points
        """
        return hypot(point2.x - self.x, point2.y - self.y)

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:
    def __init__(self, point, radius):
        
        self.centre = point
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return math.pi * self.radius * 2

# Don't add any testing code to this file!
