from  abc import ABC ,abstractmethod

class Shape(ABC):

     @abstractmethod
     def GetArea(self):
         pass


     @abstractmethod
     def getPerimetr(self):
         pass