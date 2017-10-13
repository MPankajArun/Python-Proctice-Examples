""" Function Examples """
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\tSimple Function"
#normal function
def display():
    print "Welcome to Python"
display()
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\tFunction with no resturn satatement"
#checking for return value
return_value = display()
print return_value
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\tParameter passig in functions"
#parameter passing
def add_number(num1,num2):
    result = num1 + num2
    return result
print "Addition is of 5 and 6 : " ,add_number(5,6)
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\tDefault parameters in function"
#parameter default value
def mult(num1,num2=10):     #here num2 is default and also optional and should be last
    result = num1 * num2
    return result
print "Multiplication is with default argument: ",mult(10)
print "Multiplication is with passing all arguments: ",mult(10,5)

print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\tKeyword arguments"
def greet(title,name):
    print "Hello "+title+" , "+name
    return "\n"
print "Normal function invocation : ",greet("Jhutan","Mr")
print "Invocation as keyword arguments : ",greet(name="Jhutan",title="Mr")
print "Invocation as keyword arguments : ",greet("Mr",name="Jhutan")
#print "Invocation as keyword arguments : ",greet(name="Jhutan","Mr")       #error - non keyword after Keyword
#print "Invocation as keyword arguments : ",greet("Mr",title="Mr",name="Jhutan")       #error - multiple values for keyword argument
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\nVariable number of arguments with tuple\n"
def tupleVarArg(arg1,arg2="defaultB",*theRest):
    print "formal arg1 : ",arg1
    print "Formal arg2 : ",arg2
    print "Rest of args : ",theRest

tupleVarArg('abc',123,'xyz',456.77)
print "\n"
tupleVarArg('abc',123,['xyz',456.77],['a','b']) # theRest - (['xyz', 456.77], ['a', 'b'])
print "\n"
tupleVarArg('abc')  # theRest will be empty tuple - ()
#tupleVarArg('abc',123,theRest="gg") #error
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\nVariable number of arguments with Dictionary\n"
def dictVarArg(arg1,arg2="defaultB",*therest,**theRest):
    print "formal arg1 : ",arg1
    print "Formal arg2 : ",arg2
    print "Rest of args Dict : ",theRest
    print "Rest of args Tuple : ",therest
    for i in theRest.keys():
        print "Rest ::> ",i," : " ,theRest[i]

dictVarArg('abc',123)
print "\n"
dictVarArg('abc',123,id=223,pin=44343)
print "\n"
dictVarArg('abc',4545,6454,4545,city='Pune')
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\nGlobal variables\n"
#global a
def funct1():
    global a  #same memory will be reflected for a anywhere in program after call
    a = 1
    b = 2
    print "\nInside Function:"
    print "a = ",a
    print "b = ",b
a = "One"
b = "Two"
print "\nOutside Function"
print "a = ",a
print "b = ",b
funct1()
print "\nAfter Function call"
print "a = ",a
print "b = ",b
print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print "\n\tLambda function in python\n"
a = lambda:1
print lambda:1
print a()

a = lambda num:num*2
print a
print a(6)

square = lambda(num):num**2
print "Square of 5 :" ,square(5)

print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
print (lambda:raw_input("Enter the string : ").upper())()

print "\n*:*:*:*:*:*:*:*:*:*:*:*::*:*::*:*:*:*:*::*:*:*:*:*:*::*"
