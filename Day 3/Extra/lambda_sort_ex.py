#lambda_sort_ex
from operator import itemgetter
employee_tuples = [('john','A',25),('jane','B',32),('dave','B',28)]  #list of tuples
#print sorted(employee_tuples, key=lambda student:student[2])   #sort by age

print sorted(employee_tuples, key=lambda s:s[2])   #sort by age

print "reverse = ", sorted(employee_tuples, key = itemgetter(2))
