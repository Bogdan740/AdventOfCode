import random

file = open("testinput2.txt","r")
x = file.read()
crudelist = x.split("\n")


for i in range(len(crudelist)):
    crudelist[i] = int(crudelist[i])

def checkgaps(arr):
    valid = True
    for i,val in enumerate(arr):
        try:
            if (arr[i+1] - val) > 3:
                valid = False
        except IndexError:
            pass
    return valid

arrangements = []
Clist = sorted(crudelist)

for i in range(10):
    rn = random.randint(len(Clist)-4,len(Clist))
    newList = sorted(Clist[:rn])
    print(newList)
    if newList[len(newList)-1] == 19:
        if checkgaps(newList) == True:
            if newList not in arrangements:
                arrangements.append(newList)



#print(len(arrangements))
for i in arrangements:
    print(i)
    
