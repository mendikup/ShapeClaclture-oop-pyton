from interface.shape import Shape
import math

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius


    def getArea(self):
        return (self.radius**2)* math.pi


    def getPerimeter(self):
        return self.radius * math.pi *2

