fname = '/home/pinkgeek/PycharmProjects/PY4E/mbox-short.txt'
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith('From:'): continue
    if not line.startswith('From'): continue
    words = line.split()
    count = count + 1
    print(words[1])

print("There are", count, "lines in the file with From as the first word")




