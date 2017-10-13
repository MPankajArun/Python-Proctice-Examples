listOne = [123,'abc',4.56]
print listOne
print "-----------------------------------------------------------"
tupleOne = (123,'abc',4.56)
print tupleOne
print "-----------------------------------------------------------"
print listOne[2]
listTwo = ['inner','first',listOne,56]
print listTwo
print "-----------------------------------------------------------"
tupleTwo = 'a',4,'b'
print type(tupleTwo)
print type(listTwo)
print "-----------------------------------------------------------"
print listTwo[1:3]
print listTwo[2][1]
print "-----------------------------------------------------------"
listTwo.append('ram')
print listTwo
print "-----------------------------------------------------------"
print tupleTwo[1]
print "-----------------------------------------------------------"
print tupleTwo.index('b')
print "-----------------------------------------------------------"
print listTwo.pop()
print listTwo
print "-----------------------------------------------------------"
listTwo.remove('first')
print listTwo
print "-----------------------------------------------------------"
listTwo.insert(1,'third')
print listTwo * 3
print "-----------------------------------------------------------"

listTwo.reverse()
print listTwo
print "-----------------------------------------------------------"
listTwo.sort()
print listTwo
print "-----------------------------------------------------------"
listTwo.append(56)
print listTwo.count(56)
print "-----------------------------------------------------------"
listOne.remove(123)
print listTwo
print "-----------------------------------------------------------"

print 'third' in listTwo
print "-----------------------------------------------------------"
print dir(listTwo)
print "-----------------------------------------------------------"
print dir(tupleTwo)
print "-----------------------------------------------------------"


listThree = [11,55,22,4,223,434,12,43]
print listThree
print sorted(listThree)
print "-----------------------------------------------------------"
listFour = listThree
print id(listThree)
print id(listFour)

print "-----------------------------------------------------------"
import copy
listFive = copy.deepcopy(listThree)
print id(listFive)
print listFive

print "-----------------------------------------------------------"
listThree.append(66)
print listThree
print listFive
print "-----------------------------------------------------------"

print "-----------------------------------------------------------"
