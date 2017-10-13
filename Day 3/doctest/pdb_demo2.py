import pdb
def f1(arg):
        print arg
        some_arg = arg+1
        return f2(some_arg)

def f2(arg):
        print arg
        some_arg = arg+1
        return f3(some_arg)

def f3(arg):
        print arg
        some_arg = arg+1
        return f4(some_arg)

def f4(arg):
        print arg
        some_arg = arg+1
        return some_arg

pdb.runcall(f1,1)

#b                              break point
#tbreak                         temparary break point

#http://pydev.org/updates/
