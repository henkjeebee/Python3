#Create program to read words.txt and stores them as keys in dictionary
#Use the in operator to check whether a string is present

fname = '/home/pinkgeek/PycharmProjects/PY4E/words.txt'
fhand = open(fname)
wd = {}

text = fhand.read()
words = text.split()

for word in words:
    wd[word] = None

print('continuously' in wd)


