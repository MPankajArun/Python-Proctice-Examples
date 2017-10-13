class OPair:
    def __init__(self,obj1,obj2):
        self.data = (obj1,obj2)

    def __str__(self):
        return str(self.data)
    
    __repr__ = __str__  #repr() string representation

    # Overriding the __add__()
    def __add__(self,other):
        return self.__class__(self.data[0] + other.data[0], self.data[1] + other.data[1])
    
print "-----------------------------------------------------------"
pair1 = OPair(6,99)
print "pair 1\t\t: ",pair1
pair2 = OPair(66,9)
print "pair 2\t\t: ",pair2

print "Addition\t: ",pair1 + pair2   #pair1.__add__(pair2)
print "Addition\t: ",pair1.__add__(pair2)

print "-----------------------------------------------------------"
import collections

print dir(collections)


