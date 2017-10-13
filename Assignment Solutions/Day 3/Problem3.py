import pprint

students=[]
f=open("students.csv","r")
f.readline()
for line in f:
    line=line.rstrip()
    student={}
    student['Name']=line.split(',')[0]
    student['Age']=line.split(',')[1]
    student['RollNo']=line.split(',')[2]
    student['Marks']=line.split(',')[3]
    if int(student['Age'])>20 and int(student['Marks'])>=75:
            students.append(student)
    else:
            print "Student ",student['Name']," is not eligible"
    

pp=pprint.PrettyPrinter(indent=4)
pp.pprint( students)
    
