import pickle

a = 100
b = "PSL"
c = [324,"4423",'ffd']
fin = open("state.txt","w")
pickle.dump(a,fin)
pickle.dump(b,fin)
pickle.dump(c,fin)
print "File dumped successfully"
fin.close()
print "----------------------------------------------------------"
fout = open("state.txt","r")

a1 = pickle.load(fout)
b1 = pickle.load(fout)
c1 = pickle.load(fout)
print "a1 = ",a1
print "b1 = ",b1
print "c1 = ",c1
fout.close()
print "----------------------------------------------------------"
print dir(pickle)
