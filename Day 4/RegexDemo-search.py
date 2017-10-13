import re


s1 = "PSLaaa welcome to Pune. PSL PErsistyent ..."
s2 = "Welcome to PSL ... Good Morning"

if re.search("psl",s1,re.IGNORECASE):        #match start search begining of line from first character
    print "Match found"
else:
    print "Match not found"
print "---------------------------------------------------------------"
result = re.search("PSL",s1)
if result != None:
    print"Match found = ",result.group()
else:
    print "Match not found"


"""
flags
    re.IGNORECASE
    re.MULTILINE
    re.DOTALL
"""
