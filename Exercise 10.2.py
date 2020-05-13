fname = '/home/pinkgeek/PycharmProjects/PY4E/mbox-short.txt'
fhand = open(fname)
counts = {}

#Loop through text, getting timestamps
for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    time = words[5]
    #Slice to get to the hour in the timestamp
    end = time.find(':')
    hour = time[0:end]
    # counter, add to dictionary: counts
    counts[hour] = counts.get(hour, 0) + 1

#Create a list of tuples of the dictionary counts and sort
counter = list()
for k,v in list(counts.items()):
    counter.append((k,v))
    counter.sort()

#Print sorted list, by hour:
for k,v in counter:
    print(k,v)
