file = open("day1input.txt","r")
x = file.read()
y = x.split("\n")

for i in range(len(y)):
    y[i] = int(y[i])

z = y.copy()


for i in y:
    for j in z:
        checker = i+j
        if  checker == 2020:
            wanted = i * j
        else:
            pass

print(wanted)
