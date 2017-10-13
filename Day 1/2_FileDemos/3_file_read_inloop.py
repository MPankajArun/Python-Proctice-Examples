



f = open('data.txt')
while True:
        char = f.read(1)
        if not char: break
        print char
f.close()
print "-----------------------------------------"
#as opposed to
for char in open('data.txt').read():
        print char

