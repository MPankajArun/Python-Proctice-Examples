a = [1,2,3,4]
b = [11,12,13,14]
c = [22,24,25,26]

print map(lambda x,y : x+y, a,b)
print map(lambda x,y,z : x+y*z, a,b,c)
