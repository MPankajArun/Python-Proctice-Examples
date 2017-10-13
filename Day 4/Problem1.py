import re
patt = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
validEmails = []
invalidEmails = []
fp = open("emails.txt")
for line in fp:
    line = line.rstrip()
    if re.search(patt,line) != None:
        validEmails.append(line)
    else:
        invalidEmails.append(line)
print "\tValid Emails : \n",validEmails
print "---------------------------------------------------------------"
print "\tInvalid Emails : \n",invalidEmails
fp.close()
    
