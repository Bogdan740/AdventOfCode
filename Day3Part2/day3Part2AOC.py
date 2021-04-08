file = open("day3input.txt","r")
x = file.read()
crudelist = x.split("\n")

newList = []

for i in crudelist:
    newList.append(list(i)*224)

t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0

for i in range(323):
    x = 3*i
    y = i
    checker = newList[y][x]
    if checker == "#":
        t1 +=1
    x = i
    y = i
    checker = newList[y][x]
    if checker == "#":
        t2 +=1
    x = 5*i
    y = i
    checker = newList[y][x]
    if checker == "#":
        t3 +=1
    x = 7*i
    y = i
    checker = newList[y][x]
    if checker == "#":
        t4 +=1
for i in range(162):
    x = i
    y = 2*i
    checker = newList[y][x]
    if checker == "#":
        t5 +=1
print(t1*t2*t3*t4*t5)
        


