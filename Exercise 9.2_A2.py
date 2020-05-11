fname = '/home/pinkgeek/PycharmProjects/PY4E/mbox-short.txt'
fhand = open(fname)
days = {}

for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    weekdays = words[2]

    if weekdays not in days:
        days[weekdays] = 1
    else:
        days[weekdays] = days[weekdays] + 1

print(days)