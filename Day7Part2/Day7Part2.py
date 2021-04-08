file = open("hamInput.txt","r")
x = file.read()
crudelist = x.split("\n")

outerBags = []
innerBags = []

for i in crudelist:
    helper = i.split(" ")
    outerBags.append("".join(helper[0:2]))
    secondaryBags = (" ".join(helper[3:])).split(",")
    helper3 = []
    for bag in secondaryBags:
        helper2 = bag.split(" ")
        helper2.pop()
        helper2.pop(0)
        if helper2[0] == "no":
            helper3.append("empty")
        else:
            helper3.append((int(helper2[0]),helper2[1]+helper2[2]))
            
    innerBags.append(helper3)

for i,bag in enumerate(innerBags):
    if bag == ["empty"]:
        innerBags[i] = 1

def iteration():
    for i,bag in enumerate(outerBags):
        inner = innerBags[i]
        if type(inner) != int:
            allInt = True
            totalBags = 0
            for j in inner:
                checker = innerBags[outerBags.index(j[1])]
                if type(checker) != int:
                    allInt = False
                else:
                    newVal = checker*j[0]
                    totalBags += newVal
            if allInt == True:
                innerBags[i] = totalBags + 1

while True:
    checker = outerBags.index("shinygold")
    if type(innerBags[checker]) == int:
        print(innerBags[checker]-1)
        break
    else:
        iteration()


    
    




            
            

    
       
