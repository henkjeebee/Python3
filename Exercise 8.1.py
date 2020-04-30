stuff = ['1', '2', '3', '4', '5']

def chop():
    del stuff[0]
    del stuff[-1]
    return None

def middle():
    stuff.pop(0)
    stuff.pop(-1)

middle()
print(stuff)


