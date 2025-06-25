import math

from interface.shape import Shape


class Hexagon(Shape):

    def __init__(self,side):
        self.side =side


    def getArea(self):
        return (3*math.sqrt(3) /2) * (self.side**2)

    def getPerimeter(self):
        return self.side*6