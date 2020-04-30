fname = input("Which file would you like to open: ")
try:
    fhandle = open(fname)
except:
    print("File cannot be opened ", fname)
    exit()

count = 0
total = 0

for line in fhandle:
   if line.startswith('X-DSPAM-Confidence:'):
       count = count + 1
       startpos = line.find(":")
       endpos = line.find("\n")
       confidence = line[startpos + 1:endpos]
       total = total + float(confidence)

average = total / count
print('Average spam confidence:', float(average))













