import re
num = raw_input("Enter the number")
if re.search("^[0-9]{4}$",num) != None:
    print "Number is : ",num
else:
    print "Not accepted"
    
price = raw_input("Enter the price")
if re.search("^\$[0-9]+\.[0-9]{2}$",price) != None:
    print "Price is : ",price
else:
    print "Invalid price"
