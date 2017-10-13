
import pprint
f=open("country.txt","r")

countryDict = {}


for line in f:
        line=line.rstrip()
        lang=line.split(',')[-1]
        if lang in countryDict:
                countryDict[lang][line.split(',')[0]]=[]
                countryDict[lang][line.split(',')[0]].append(line.split(',')[2])
                
        else:
                countryDict[lang]={}
                countryDict[lang][line.split(',')[0]]=[]
                countryDict[lang][line.split(',')[0]].append(line.split(',')[2])
                

pp=pprint.PrettyPrinter(indent=4)
for i in countryDict.keys():
    print (i,":",countryDict[i])

print"\n\n"
pp.pprint (countryDict)




