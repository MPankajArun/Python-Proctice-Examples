emp ={'1a':30000,'2a':40000}
keysList = emp.keys()
keysList.sort()
print "Sorted Keys : ",keysList

print "Employee Details"
for i in keysList:
    print i,":",emp[i]

print "Updated Employee Details"
for i in keysList:
    print i,":",emp[i]+5000
