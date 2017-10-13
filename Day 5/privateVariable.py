class Counter:
    __count = 0
    def getCounter(self):
        self.__count += 1
        print self.__count

print "-----------------------------------------------------------"

counter = Counter()
counter.getCounter()
counter.getCounter()

# print counter.__count - ERROR
print counter._Counter__count
print "-----------------------------------------------------------"
