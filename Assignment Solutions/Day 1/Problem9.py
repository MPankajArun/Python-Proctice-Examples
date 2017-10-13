import calendar
year = input("Enter the year : ")
if calendar.isleap(year):
    print "%s is Leap year." %year
else:
    print "%s is not Leap Year." %year
