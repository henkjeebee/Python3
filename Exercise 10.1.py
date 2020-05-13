fname = '/home/pinkgeek/PycharmProjects/PY4E/mbox-short.txt'
fhand = open(fname)
prolif = {}

for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    #Gets the emailaddress from the line
    sender = words[1]
    #counter, add to dictionary: prolif
    prolif[sender] = prolif.get(sender, 0) + 1

#Create a list of tuples of the dictionary prolif and sort
prolist = list()
for k,v in list(prolif.items()):
    prolist.append((v,k))
    prolist.sort(reverse=True)

#Print tuple sub 0:
for k,v in prolist[:1]:
    print(k,v)