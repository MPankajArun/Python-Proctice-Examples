class Parent:
    'Parent Class'
    pi = 3.1471
    def __init__(self):
        print "Created an instance of Parent - " ,self.__class__.__name__
    def greet(self):
        print "Hi, I am Prent-greet"

class Child(Parent):
    'Child Class'
    def __init__(self):
        print "Created an instance of Child - ",self.__class__.__name__
    def greet(self):
        print "Hi, I am Child-greet"
      
    

print "-------------------------------------------------------------"

p = Parent()
print "Class that got created = ",p.__class__
print "Parent class if any = ",Parent.__bases__
print "Doc string if any = ",Parent.__doc__
print "class attributes of class = ",dir(Parent)
print "Calling Parent class method - ",p.greet()
print "-------------------------------------------------------------"

c =Child()
print "Class that got created = ",c.__class__
print "Parent class if any = ",Child.__bases__
print "Doc string if any = ",Child.__doc__
print "class attributes of class = ",dir(Child)
print "Calling Child class method - ",c.greet()
print "-------------------------------------------------------------"
print "Is class Child subclass of Parent - ",(issubclass(Child, Parent))
print "Is class Parent subclass of Child - ",(issubclass(Parent, Child))
print "-------------------------------------------------------------"
print "Is Object c instnce of Parent - ",isinstance(c,Parent)
print "Is Object c instnce of Child - ",isinstance(c,Child)
print "-------------------------------------------------------------"
print "Calling method from base class with child class obj"
Parent.greet(c)     
print "-------------------------------------------------------------"
