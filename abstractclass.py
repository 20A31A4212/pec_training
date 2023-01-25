from abc import ABC,abstractmethod

class Area(ABC): #it is an abstract class
    @abstractmethod #annotation
    def calculate_area(self): #it is an abstract method
        pass
    @abstractmethod
    def calculate_circle_area(self): #it is an abstract method
        pass


class Square(Area):
    def calculate_area(self):
        print("in square calculate_area method")
    def calculate_circle_area(self): """it is an abstractmethod we must have to define it (if we no need it)
        pass                          ,if not written gives error"""


class Circle(Area):
    def calculate_area(self):
         print("in circle calculate_area method")
    def calculate_circle_area(self):
        print("in circle calculate_circle area method")

ob=Square()
ob.calculate_area()
ob.calculate_circle_area()

ob1=Circle()
ob1.calculate_area()
ob1.calculate_circle_area()






