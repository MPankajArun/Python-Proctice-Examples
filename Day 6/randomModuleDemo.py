import random
import glob

lst = [4,5,3,76,45,2,323,66]
print "Original List : ",lst
print "----------------------------------------------------------"
random.shuffle(lst)
print "Random List   : ",lst
print "----------------------------------------------------------"
print "Randome choice from list : ",random.choice(lst)
print "----------------------------------------------------------"
print "Random float number : ",random.random()
print "----------------------------------------------------------"
print "Random range : ",random.randrange(9)
print "----------------------------------------------------------"
print glob.glob("*.txt")
print "----------------------------------------------------------"
