fname = '/home/pinkgeek/PycharmProjects/PY4E/mbox-short.txt'
fhand = open(fname)
days = {}

for line in fhand:
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    if line == '': continue
    words = line.split()
    weekdays = words[2]
    print(weekdays)
    days[weekdays] = 0
for i in days:
        if i not in days:
            days[i] = 1
        else:
            days[i] = days[i] + 1'''

print(days)


