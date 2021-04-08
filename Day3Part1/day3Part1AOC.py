file = open("day3input.txt","r")
x = file.read()
crudelist = x.split("\n")

newList = []

for i in crudelist:
    newList.append(list(i)*32)

x = 0
y = 0

print(newList[0])

trees = 0;
for i in range(323):
    x = 3*i
    y = i
    checker = newList[y][x]
    if checker == "#":
        trees +=1

print(trees)
        


