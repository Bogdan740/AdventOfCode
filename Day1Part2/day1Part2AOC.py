file = open("day1input.txt","r")
x = file.read()
y = x.split("\n")

for i in range(len(y)):
    y[i] = int(y[i])

z = y.copy()
w = y.copy()


for i in y:
    for j in z:
        for k in w:
            checker = i+j+k
            if  checker == 2020:
                wanted = i * j * k
            else:
                pass

print(wanted)
