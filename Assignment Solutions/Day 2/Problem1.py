

fin=open('country.txt','r')
data =fin.readlines()   #list of all lines
countryDict = {}
#print data
for line in data:
    #print line.split(',')[-1]
    lang = line.split(',')[-1][:-1]
    country = line.split(',')[0]
    if (countryDict.has_key(lang)):
        countryDict[lang].append(country)
    else:
        countryDict[lang] = [country]

print countryDict
print "---------------------------------------------------------------"
for i in countryDict.keys():
    print i," : ",countryDict[i]
fin.close()
