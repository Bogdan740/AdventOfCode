file = open("testinput.txt","r")
x = file.read()
crudelist = x.split("\n")


for i in range(len(crudelist)):
    crudelist[i] = int(crudelist[i])

for i in crudelist:
    print(i)
