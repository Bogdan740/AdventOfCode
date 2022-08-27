from random import randint

file = open("day9input.txt","r")
x = file.read()
crudelist = x.split("\n")


for i in range(len(crudelist)):
    crudelist[i] = int(crudelist[i])

invalidNum = 1504371145

wantedList = []
while True:
    pos = randint(0,len(crudelist))
    ints = randint(0,len(crudelist))
    try:
        newList = crudelist[pos:ints]
        helper = sum(newList)
        if helper == invalidNum:
            if newList[0] != invalidNum:
                print(newList)
                wantedList = newList
                break
    except IndexError:
        pass
a = sorted(wantedList)
b= a[len(a)-1]+a[0]
print(b)
