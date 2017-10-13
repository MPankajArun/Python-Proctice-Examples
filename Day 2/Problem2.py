"""def long_words(n,str1):
    longWordsList=[]
    words = str1.split(' ')
    for i in words:
        if len(i) > n:
            longWordsList.append(i)
    return longWordsList

print(long_words(3,"The quick brown fox jumps over the lazy dog"))
"""
longWords = lambda : [i for i in raw_input("Enter the String ").split(' ') if len(i) >3 ]
print longWords()
