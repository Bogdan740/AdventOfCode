file = open("day7input.txt","r")
x = file.read()
crudelist = x.split("\n")



outerBags = []
innerBags = []


for i in crudelist:
    helper = i.split(" ")
    outerBags.append("".join(helper[0:2]))
    secondaryBags = (" ".join(helper[4:])).split(",")
    for j,bag in enumerate(secondaryBags):
        helper2 = bag.split(" ")
        helper2.pop()
        if(j == 0):
            helper2.pop(0)
        else:
            helper2.pop(1)
        secondaryBags[j] = "".join(helper2)
    innerBags.append(secondaryBags)

bags = {}

for i,bag in enumerate(outerBags):
    bags.update({bag:innerBags[i]})


#for i,bag in enumerate(outerBags):
    #print(bag, " :" , innerBags[i])

allbags = []

def bagInbag(main,inner,confirmed):
    checker = []
    for i,bagM in enumerate(main):
        bagI = inner[i]
        for j in bagI:
            if j in confirmed and j not in checker:
                checker.append(bagM)
    return checker

sgBags = []
a = outerBags
b = innerBags
c = ["shinygold"]
checker = bagInbag(a,b,c)

c = 0
while True:
    oldsgbags = sgBags.copy()
    for i in checker:
        if i not in sgBags:
            sgBags.append(i)
    if sgBags == oldsgbags:
        print(len(sgBags))
        break
    else:
        checker = bagInbag(a,b,checker)
    
    
    



            
            

    
       
