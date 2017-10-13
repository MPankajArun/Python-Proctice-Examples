import sys
import os

if(os.path.exists("hello.txt")):
    sys.stderr.write("File already exists")
    os.remove("hello.txt")
    sys.exit(1)
f = open("hello.txt","w")
f.write("hello world\n")
f.close()
f = open("hello.txt","r")
print "----------------------------------------------------------"
while True:
    x = f.readline()
    if x:
        print x
    else:
        break

os.rmdir("temp")
print "----------------------------------------------------------"
print os.listdir('.')
print "----------------------------------------------------------"
os.mkdir("temp")
print os.listdir('.')
print "----------------------------------------------------------"

temp = sys.stdout
f = open("error.txt","w")
sys.stdout = f
print "More fun More work"
print "----------------------------------------------------------"
sys.stdout = temp
f.close()
print "Fun is good"
print "----------------------------------------------------------"
print sys.version
print "----------------------------------------------------------"
if int(str(sys.version).split('.')[0])==2:
    print "Varsion 2"
else:
    print "Not supported"
print "----------------------------------------------------------"
