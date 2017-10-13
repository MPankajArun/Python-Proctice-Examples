"""Iter_Demo.py"""
# iter.py

str = "formidable"   #str[0]

for i in str:    #for loop traverses all elements in a sequence
   print i,

print "------------------------------------------"

it = iter(str)   #iter is predenfined function

print it.next()
print it.next()
print it.next()
print "------------------------------------------"
print "List retirived from it object = ",list(it)

s1 ={1,2,3,4,5}   #this is not a sequence type data
it1 = iter(s1)
print "set element = ", it1.next()
print "set element = ", it1.next()
print "set element = ", it1.next()
print "set element = ", it1.next()
print "set element = ", it1.next()
print "set element = ", it1.next()

