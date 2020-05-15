#A simple Pyhton-script that simulates grep

import re
fname = '/home/pinkgeek/PycharmProjects/PY4E/mbox.txt'
fhand = open(fname)
regex = input('Enter a regular expression: ')
counter = 0

#Search through line, looking for matches of inputted regular expression
for line in fhand:
    line = line.rstrip()
    expr = re.findall(regex, line)
    #If line is not empty, add 1 to the counter
    if len(expr) > 0: counter = counter + 1

print("mbox.txt had ", counter, "lines that matched ", regex)