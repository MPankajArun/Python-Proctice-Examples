class Parent1:
    'Parent 1 Class'
    
    def __init__(self):
        print "Created an instance of Parent 1 - " ,self.__class__.__name__
    def greet(self):
        print "Hi, I am Prent1 - greet"
print "-------------------------------------------------------------"        
class Parent2:
    'Parent 2 Class'
    
    def __init__(self):
        print "Created an instance of Parent 2 - " ,self.__class__.__name__
    def greet(self):
        print "Hi, I am Prent2 - greet"
    def show(self):
        print "Parent 2 - Welcome to Pune"
print "-------------------------------------------------------------"
class Child1(Parent1,Parent2):
    'Child 1 Class'
    def __init__(self):
        print "Created an instance of Child 1 - ",self.__class__.__name__
    pass
print "-------------------------------------------------------------"
class Child2 (Parent1 ,Parent2):
    'Child 2 Class'
    def __init__(self):
        print "Created an instance of Child 2 - ",self.__class__.__name__
    def greet(self):
        print "Hi, I am Child 2 - greet"
    def show(self):
        print "Child 2 - Welcome to Pune"
print "-------------------------------------------------------------"     
class GrandChild(Child1,Child2):
    'Grand Child Class'
    pass

print "-------------------------------------------------------------"
gc = GrandChild()
gc.greet()
gc.show()
Child2.show(gc)
print "-------------------------------------------------------------"
