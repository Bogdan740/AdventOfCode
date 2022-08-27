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
        




goodPass = []

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
        goodPass.append(i)

def checkByr(year):
    if year>= 1920 and year <=2002:
        return 1
    else:
        return 0
    
def checkIssue(year):
    if year>=2010 and year<=2020:
        return 1
    else:
        return 0

def checkExpiration(year):
    if year>=2020 and year<=2030:
        return 1
    else:
        return 0

def checkCM(height):
    if height >= 150 and height<=193:
        return 1
    else:
        return 0
def checkIN(height):
    if height>=59 and height <= 76:
        return 1
    else:
        return 0

def checkHair(hair):
    allowedChars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    checker = list(hair)
    isValid = 1
    for i in checker:
        if i in allowedChars:
            pass
        else:
            isValid = 0
    return isValid

def checkPID(pid):
    allowedChars = ["0","1","2","3","4","5","6","7","8","9"]
    checker = list(pid)
    isValid = 1
    for i in checker:
        if i in allowedChars:
            pass
        else:
            isValid = 0
    return isValid

def checkECL(ecl):
    allowedCols = ["amb","blu","brn","gry","grn","hzl","oth"]
    checker = list(ecl)
    isValid = 1
    if len(checker) == 3:
        if ecl in allowedCols:
            pass
        else:
            isValid = 0
    if len(checker) == 4:
        if ecl[:-1] in allowedCols:
            pass
        else:
            isValid = 0
    return isValid
        
legalPass = 0

for i in goodPass:
    counter = 0

    pos = i.find("byr") + 4
    birth = int(i[pos:pos+4])
    counter += checkByr(birth)

    pos = i.find("iyr") + 4
    issue = int(i[pos:pos+4])
    counter += checkIssue(issue)

    pos = i.find("eyr") +4
    expiration = int(i[pos:pos+4])
    counter += checkExpiration(expiration)

    pos = i.find("hgt")
    verifyCM = i[pos+7:pos+9]
    verifyIN = i[pos+6:pos+8]
    if verifyCM == "cm":
        height = int(i[pos+4:pos+7])
        counter += checkCM(height)
    if verifyIN =="in":
        height = int(i[pos+4:pos+6])
        counter += checkIN(height)

    pos = i.find("hcl")
    counter += checkHair(i[pos+5:pos+11])

    pos = i.find("pid")
    counter += checkPID(i[pos+4:pos+13])

    pos = i.find("ecl")
    counter += checkECL(i[pos+4:pos+8])
    print(i[pos+4:pos+8])

    if counter == 7:
        legalPass +=1

print(legalPass)
        
    
        



                           
