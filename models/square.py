from interface.shape import Shape

class Square(Shape):

    def __init__(self, side):
        self.side=side



    def getArea(self):
        return self.side**2


    def getPerimeter(self):
        return self.side*4



