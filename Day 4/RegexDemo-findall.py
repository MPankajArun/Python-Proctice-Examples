import re

patt =r"PSL"
s1 = "PSLaaa welcome to Pune. PSL PErsistyent ..."
s2 = "Welcome to PSL ... Good Morning PSL"

m = re.findall(patt,s1)
#print "m = ",m
if m != None: #match start search begining of line from first character
    print patt ,"Occures " ,len(m) ,"time"
    print "Match found as = ",m 
else:
    print "Match not found"
print "---------------------------------------------------------------"
print re.findall("car","car")
print re.findall("car","scary")
print re.findall("car","carry the tarcardi to the car")
print "---------------------------------------------------------------"
