import pdb
#python debugging
def test_deb(test_val):
	print "start test val is ", test_val
	ret_val = test_val/10
	print "end test_val is ", test_val
	return ret_val

#print test_deb(20)   #function call

pdb.run("test_deb(20)")   #invoking function test_deb(20) by run on pdb





#execute the file
#it goes into pdb prompt
# keep pressing s
# then type\# p test_val
#p ret_val
# s shows the line of code to be executed
