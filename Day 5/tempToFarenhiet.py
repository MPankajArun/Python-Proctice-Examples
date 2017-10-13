def convertToFarenheit(temp):
    return (float(9)/5) * temp + 32
def convertToCelcius(temp):
    return (float(9)/5) * (temp - 32)
print "----------------------------------------------------------------"
temp = [36.5,37,37.5,39]
farh = map(convertToFarenheit,temp)
print "Farenheit\t: ",farh
celcius = map(convertToCelcius,farh)
print "Celciuss\t: ",celcius
print "----------------------------------------------------------------"

print "Farenheit using lamda\t: ",map(lambda x:(float(9)/5) * x + 32,temp)
print "Celciuss using lamda\t: ",map(lambda x:(float(9)/5) * (x - 32),farh)
print "----------------------------------------------------------------"
