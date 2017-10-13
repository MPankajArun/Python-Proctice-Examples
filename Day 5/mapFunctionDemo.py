lst = range(10)
print "Original List\t\t\t: ",lst
print "Using List Comprehension \t: ",[i**2 for i in lst]
print "Using map() & lambda expression : ",map((lambda i : i**2),lst)
