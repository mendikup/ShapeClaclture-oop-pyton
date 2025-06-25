from  abc import ABC ,abstractmethod

class Shape(ABC):

     @abstractmethod
     def getArea(self):
         pass


     @abstractmethod
     def getPerimeter(self):
         pass