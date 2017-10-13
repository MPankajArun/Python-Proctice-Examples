class Birds:
    def __init__(self):
        ''' Contstructor '''
        self.members = ['Sparrow','Robin','Duck','Crow']
    def printMembers(self):
        print "Printing Memebers of Birds class"
        for member in self.members:
            print('\t%s '%member)

if __name__ == "__main__":
    b1 = Birds()
    b1.printMembers()
