lst = range(50)
print "Numbers Divisible by 4  : ",filter(lambda i:i%4==0, lst)

def evenCheck(x):
    return x%2==0
print "Even Numbers \t\t: ",filter(evenCheck, lst)


words = ["abc","xyz","NIL","AMN"]
#print [i for i in words if i.isupper()]

print "Only Uppercase Words : ",filter(lambda i:i.isupper(),words)
