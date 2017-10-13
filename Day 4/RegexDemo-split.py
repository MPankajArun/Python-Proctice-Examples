import re

str1 = "Good: bad:better::worse: 9best:worst"
print str1
print "--------------------------------------------------------------"
print re.split(":{2}",str1)
print "--------------------------------------------------------------"
print re.split(":",str1)
print "--------------------------------------------------------------"
print re.split("\d",str1)
print "--------------------------------------------------------------"
str2 = "This is just testing. this is aa123dd just tesing. godd Morning"
print [i for i in re.split("\s+",str2) if re.search("^[a-z]+$",i) != None]
print "--------------------------------------------------------------"

f=open("data.txt","r")
words= []
for line in f:
   words.extend([i for i in re.split("\s+",line) if re.search("^Persistent$",i)!= None])
print "Persistent occures in file ",len(words)," times" 
print "--------------------------------------------------------------"

str3 = "Persistent Systems Launches Engineering Services for IBM Watson IoT"
print "Original : ",str3
regexp = re.compile("Persistent Systems")
print "Modified : ",regexp.sub("PSL",str3)
print "--------------------------------------------------------------"

