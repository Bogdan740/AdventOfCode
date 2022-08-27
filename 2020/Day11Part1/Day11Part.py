file = open("input.txt","r")
x = file.read()
crudelist = x.split("\n")

for i in crudelist:
    print(i)
