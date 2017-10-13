class SayHello:
    def __init__(self):
        print "Inside Constructor = ",self
        self.greeting = "Hello, How are you ?"

    def displayGreeting(self):
        return self.greeting
print "-----------------------------------------------------------------"
# Object Instantiation
hello1 = SayHello()
print "Object 1 = ",hello1
print "Greeting From Class Instance Memmber: ",hello1.greeting
print "Greeting From Class Method: ",hello1.displayGreeting()
print "-----------------------------------------------------------------"
hello2 = SayHello()
print "Object 2 = ",hello2
print "Greeting From Class Instance Memmber: ",hello2.greeting
print "Greeting From Class Method: ",hello2.displayGreeting()
print "-----------------------------------------------------------------"
