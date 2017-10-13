
import pprint


class invalidAgeError(Exception):
    pass




f=open("empdata.txt")

employees=[]

for line in f.readlines():
    line=line.rstrip()
    emp={}
    emp['Id']=line.split(":")[0]
    emp['Name']=line.split(":")[1]
    emp['Age']=line.split(":")[2]
    emp['Salary']=line.split(":")[3]
    try:
        if(int(emp['Age'])<18):
            msg="entry",emp['Id'],"Skipped due to Inappropriate age"
            raise invalidAgeError(msg)
        else:
            employees.append(emp)
           
    except invalidAgeError as e:
        print e
        
    
pp=pprint.PrettyPrinter(indent=4)
pp.pprint (employees)

