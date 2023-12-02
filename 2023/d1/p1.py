lines = None
with open("input.txt") as fp:
    lines = fp.readlines()

s = 0
for line in lines:
    first = None
    last = None
    for char in line:
        if(char.isdigit()):
            if(first == None):
                first = char
                last = char
            else:
                last = char
    s += int(first+last)

print(s)