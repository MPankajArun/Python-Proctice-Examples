import re
str4 = "Welcom\n3to Pune. Good Morning."
m = re.search("([a-zA-z]+)(\s+)([a-zA-Z]+)",str4)
if m!= None:
    print "MAthch found : ",m.group()
    print "MAthch found : ",m.group(0)
    print "MAthch found : ",m.group(1)
    print "MAthch found : ",m.group(2)
    print "MAthch found : ",m.group(3)
    print "MAthch found : start - ",m.start(), " End -" , m.end()
else:
    print "MAtch not found"
print "--------------------------------------------------------------"
    
regexp = r"([a-zA-z]+ \d)"
matches = re.finditer(regexp,"June 24,August 09,May 20")
print "Match List Object :", matches
for match in matches:
    print "match at index: %s, %s" %(match.start(),match.end())
