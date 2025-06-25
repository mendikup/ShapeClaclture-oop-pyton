from interface.shape import Shape

class Rectangle(Shape):

    def __init__(self , length,width ):
        self.length=length
        self.width=width

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return (self.width+self.length) * 2



