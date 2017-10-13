import math
class Circle:
    pi = math.pi
    allCircles = []
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

    @classmethod
    def total_area(cls):
        total = 0
        for c in Circle.allCircles:
            total = total + c.area()
        return total


if __name__ == "__main__":
    print "------------------------------------------------------------"
    c1 = Circle()
    c1.setRadius(input("Enter the radiius of Circle "))
    print "Area of circle of radius %s is %s" %(c1.getRadius(),c1.area())
    Circle.allCircles.append(c1)
    print "------------------------------------------------------------"
    c2 = Circle()
    c2.setRadius(input("Enter the radiius of Circle "))
    print "Area of circle of radius %s is %s" %(c2.getRadius(),c2.area())
    Circle.allCircles.append(c2)
    print "------------------------------------------------------------"
    c3 = Circle()
    #c2.setRadius(input("Enter the radiius of Circle "))
    print "Area of circle of radius %s is %s" %(c3.getRadius(),c3.area())
    Circle.allCircles.append(c3)
    print "------------------------------------------------------------"
    Circle.test()
    print "------------------------------------------------------------"
    print "Total area of all Circle is = ",Circle.total_area()
    print "------------------------------------------------------------"
