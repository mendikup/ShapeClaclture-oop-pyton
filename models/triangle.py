from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def getArea(self):
        return 0.5 * super().getArea()

    def getPerimeter(self):

        return None


