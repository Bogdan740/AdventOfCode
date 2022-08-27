file = open("day4input.txt","r")
x = file.read()
crudelist = x.split("\n")



newList = []
ints = []
for i in range(len(crudelist)):
    if crudelist[i] != "":
        ints.append(i)
    elif crudelist[i] == "":
        helper = ""
        for j in ints:
            helper = helper + crudelist[j]
        newList.append(helper)
        ints = []
        



print(newList)
goodPass = 0
for i in newList:
    checker = 0
    birth = i.count("byr")
    if birth >0:
        checker +=1
    issue = i.count("iyr")
    if issue >0:
        checker +=1
    expiry = i.count("eyr")
    if expiry >0:
        checker +=1
    height = i.count("hgt")
    if height >0:
        
        checker +=1
    hair = i.count("hcl")
    if hair >0:
        checker +=1
    eye = i.count("ecl")
    if eye >0:
        checker +=1
    pid = i.count("pid")
    if pid >0:
        checker +=1
    if checker == 7:
        goodPass +=1
print(goodPass)
    
    
        
    

