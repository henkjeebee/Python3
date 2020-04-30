filename = input("Which file would you like to open: ")
try:
    filehandle = open(filename)
except:
    print("File cannot be opened ", filename)
    exit()

inp = filehandle.read()
for line in inp:
    line = line.rstrip()
caps = inp.upper()
print(caps)


