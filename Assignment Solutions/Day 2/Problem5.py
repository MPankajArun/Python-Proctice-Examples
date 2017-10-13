my_dict={'x':500,'y':5874,'z':560}

print max([i for i in my_dict.values()])
print min([i for i in my_dict.values()])

print max(my_dict.values(), key=lambda x: int(x))
print min(my_dict.values(), key=lambda x: int(x))
