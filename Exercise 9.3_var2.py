fname = '/home/pinkgeek/PycharmProjects/PY4E/mbox-short.txt'
fhand = open(fname)
prolif = {}

for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    sender = words[1]

    prolif[sender] = prolif.get(sender,0) + 1

print(prolif)