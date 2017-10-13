class SayHello:
    def __init__(self,arg):
        print "Inside Constructor = ",self
        self.greeting = "Hello " +arg +", How are you ?"

    def displayGreeting(self):
        return self.greeting

    def convertUpper(self):
        return self.greeting.upper()
    
print "-----------------------------------------------------------------"
# Object Instantiation
hello1 = SayHello("Saddam")
print "Object 1 = ",hello1
print "Greeting From Class Instance Memmber: ",hello1.greeting
print "Greeting From Class Method: ",hello1.displayGreeting()
print "Greeting From Class Method: ",hello1.convertUpper()
print "-----------------------------------------------------------------"
hello2 = SayHello("Jhutan")
print "Object 2 = ",hello2
print "Greeting From Class Instance Memmber: ",hello2.greeting
print "Greeting From Class Method: ",hello2.displayGreeting()
print "Greeting From Class Method: ",hello2.convertUpper()
print "-----------------------------------------------------------------"
