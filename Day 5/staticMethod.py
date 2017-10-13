import math
class Circle:
    pi = math.pi
    def __init__(self):
        self.radius = 1
    
    def setRadius(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius

    
    def area(self):
        return Circle.pi * (self.radius ** 2)

    @staticmethod
    def test():
        print "Inside static method"
        print "Value of PI = ",Circle.pi


if __name__ == "__main__":
    print "------------------------------------------------------------"
    c1 = Circle()
    c1.setRadius(input("Enter the radiius of Circle "))
    print "Area of circle of radius %s is %s" %(c1.getRadius(),c1.area())
    print "------------------------------------------------------------"
    c2 = Circle()
    c2.setRadius(input("Enter the radiius of Circle "))
    print "Area of circle of radius %s is %s" %(c2.getRadius(),c2.area())
    print "------------------------------------------------------------"
    c2 = Circle()
    #c2.setRadius(input("Enter the radiius of Circle "))
    print "Area of circle of radius %s is %s" %(c2.getRadius(),c2.area())
    print "------------------------------------------------------------"
    Circle.test()
    print "------------------------------------------------------------"

