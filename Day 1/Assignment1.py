"""
Accept string from user
    1) check for palindrome
    2) make uppercase
    3) print the count of substring in that string

"""

str1 = raw_input("Enter the input string : ")
rev = str1[::-1]

if(str1 == rev):
    print "%s is palindrome." %str1
else:
    print "%s is not palindrome." %str1

print "Input in Uppercase : ",str1.upper()

sub = raw_input("Enter the input chars : ")
count = str1.count(sub,0)
print "count of %s in %s is : " %(sub,str1),count
