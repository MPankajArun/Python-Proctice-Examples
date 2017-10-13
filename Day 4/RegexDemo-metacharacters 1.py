import re
"""
METACHARACTERS
    .  => searches for any one character except "\n" ex. "PSL."

    +  => 1 or more occurences

    ?  => 0 or 1 only occurences

    *  => 0 or more occurences

    |  => search for alternative search  ex. "Pune|PSL"

    [] => match any single character from character class  ex. [A-Za-z0-9],[^A-Z]

    {} => match N to M occurence preceding to RE ex. xy{2}z -> xyyz

    () => match enclode subgroup 

    ^  => find match at begginnig ex. "^PSL"

    $  => is for the end search  ex. "PSL$"

"""
patt ="(to)*"
s1 = "PSLaaa Welcome to Pune. a1 PSL PErsistyent ..."
s2 = "welcome To Pune ... 24192 Good Morning PSL."

m = re.search(patt,s1)
#print "m = ",m
if m != None: 
    
    print "Match found as = ",m.group()
else:
    print "Match not found"
print "---------------------------------------------------------------"
n = re.search("[0-9]",s2)
#print "m = ",m
if n != None: 
    print "Match found as = ",n.group()
else:
    print "Match not found"
print "---------------------------------------------------------------"
print re.findall("car","car")
print re.findall("car","scary")
print re.findall("car","carry the tarcardi to the car")
print "---------------------------------------------------------------"


"""
1: accept 4 digit number and validate it
2: accept a number  as a price field for ex. 1.55
    start with $
    after $ atleast 1 digit
    exact 2 digit after decimal

"""
