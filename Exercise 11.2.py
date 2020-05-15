import re
fname = input("Enter file: ")
fhand = open(fname)
lst = []

for line in fhand:
    #Uses regular expression to find all "New Revision:" lines and the number:
    regex = re.findall('^New Revision:.* ([0-9.]+)', line)
    #Skip empty results
    if len(regex) > 0:
        #Extract the integer from the result of the regular expression
        for digit in regex:
            digit = int(digit)
        #Append matching integers to the list
        lst.append(digit)

#Calculate average: sumtotal of list divided by the # of items in the list
average = sum(lst) / len(lst)
print(average)

