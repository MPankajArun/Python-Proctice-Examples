#write to file
#f = open("c:\\data\\myfile.txt", "a")             #file  object created in write mode

f = open("myfile.txt", "a")             #file  object created in write mode
print dir(f) #list of all attributes and functions of passed object

print "-------------------------------------------------------------------"
f.write("Welcome to Persistent\n")

f.write("Good Morning\n")
f.write("Have a Good day\n")
f.close();

print "----------------------------------------------------------------------------------"























"""

print "-------------------------------------------------------------------"
str = "Hello"
print dir(str)
print "-------------------------------------------------------------------"
l1=[1,2,3]
print dir(l1)
print "-------------------------------------------------------------------"
"""
