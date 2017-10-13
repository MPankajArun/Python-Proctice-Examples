def reading(filePath,n):
    try:
        try:
            print "Inside Inner Try block"
            fp = open(filePath)
            x = 4/n
        except IOError as e:
            print "\tOops ...",e
        except Exception as a:
            print "\tError - ", a
        finally:
            print "\tInside finally block"
        print "Inside Outer Try block"
        print z
    except Exception as e:
        print "\tOther Error - ",e
    finally:
        print "\tOuter Finally block"

    
print "---------------------------------------------------------------"
print "\n\t\t\tException Handling Demo\n"
print "---------------------------------------------------------------"
reading("abc.txt",2)
print "---------------------------------------------------------------"
reading("data.txt",0)
print "---------------------------------------------------------------"
reading("data.txt",2)
print "---------------------------------------------------------------"
reading("abc.txt",0)
print "---------------------------------------------------------------"
try:
    reading()
except Exception as e:
    print "Error - ",e
print "\n\t\t\t\tEND"
print "---------------------------------------------------------------"
