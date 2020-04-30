fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
     if line == '' or if words[0] != 'From':
        print('Debug:', words)
    #print(words[2])
