#In the example above we haven't used lambda. By using lambda,
#we wouldn't have had to define and name the functions fahrenheit() and celsius().
Celsius = [39.2, 36.5, 37.3, 37.8]
print "Original temp in Celsius =", Celsius         #Original temp in Celsius = [39.2, 36.5, 37.3, 37.8]

Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print "Fahrenheit temp using map and lambda =", Fahrenheit  #Fahrenheit temp using map and lambda = [102.56, 97.7, 99.14, 100.03999999999999]

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print "Celsius temp using map and lambda =", C       #Celsius temp using map and lambda = [39.2, 36.5, 37.300000000000004, 37.8]
 
"""
>>> f = lambda x, y : x + y
>>> f(1,1)
"""
