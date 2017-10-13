class Mammals:
    def __init__(self):
        ''' Contstructor '''
        self.members = ['Tiger','Elephant','Bear','Wolf']
    def printMembers(self):
        print "Printing Memebers of Mammals class"
        for member in self.members:
            print('\t%s '%member)

if __name__ == "__main__":
    m1 = Mammals()
    m1.printMembers()
