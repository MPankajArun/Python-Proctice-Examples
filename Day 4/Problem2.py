import re
patt = r"^(http|ftp|file)(://)([w]{3})\.([a-zA-Z]+)\.(com)$"
validURLs = []
fp = open("urls.txt")
for line in fp:
    line = line.rstrip()
    if re.search(patt,line) != None:
        validURLs.append(line)
    
print "\tValid URLs : \n",validURLs
print "---------------------------------------------------------------"
fp.close()
    
