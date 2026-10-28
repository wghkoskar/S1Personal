import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def distance(self):

        return hypot(self.x, self.y)

    def distance_to(self, point2):

        return hypot(point2.x - self.x, point2.y - self.y)

class Circle:

    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def circumference(self):
        return 2 * math.pi * self.radius
