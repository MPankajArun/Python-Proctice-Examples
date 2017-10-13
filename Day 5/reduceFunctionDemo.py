lst = ['h','e','l','l','o']
print "Complete word built from characters : ",reduce(lambda i,j:i+j,lst)
print "-----------------------------------------------------------------"
lis = [ 1 , 3, 5, 6, 2, ]
print "The sum of the list elements is : ",reduce(lambda a,b : a+b,filter(lambda x:x>3,lis))
