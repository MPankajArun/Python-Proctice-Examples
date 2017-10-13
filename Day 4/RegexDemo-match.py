import re

regexp = re.compile("PSL")
s1 = "PSLaaa welcome to Pune. PSL PErsistyent ..."
s2 = "Welcome to PSL ... Good Morning"

if regexp.match(s1):        #match start search begining of line from first character
    print "Match found"
else:
    print "Match not found"
print "---------------------------------------------------------------"
if regexp.match(s2):
    print "Match found"
else:
    print "Match not found"
