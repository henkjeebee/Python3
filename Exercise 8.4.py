fname = '/home/pinkgeek/PycharmProjects/PY4E/romeo.txt'
fhand = open(fname)

#Create a list of words and sort
inp = fhand.read()
textlist = inp.split()
textlist.sort()
newtext = []

for word in textlist:
    #Check if word is unique
    if word not in newtext:
        newtext.append(word)

print(newtext)



