

fin=open('country.txt','r')
data =fin.readlines()   #list of all lines
countryDict = {}
#print data
for line in data:
    #print line.split(',')[-1]
	lang = line.split(',')[-1][:-1])
    if (countryDict.has_key():
        countryDict[lang] += 1
    else:
        countryDict[lang] = 1

print countryDict
print "---------------------------------------------------------------"
for i in countryDict.keys():
    print i," : ",countryDict[i]
fin.close()
