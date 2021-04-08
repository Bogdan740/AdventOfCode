file = open("day2input.txt","r")
x = file.read()
crudelist = x.split("\n")


verificators = []
passwords = []

for i in crudelist:
    helper = i.split(":")
    verificators.append(helper[0])
    passwords.append(helper[1])


validPass = 0
for i in range(len(passwords)):
    helper = verificators[i].split("-")
    lower = int(helper[0])
    helper2 = helper[1].split(" ")
    upper = int(helper2[0])
    letter = helper2[1]
    passChecker = list(passwords[i])
    total = 0
    for j in passChecker:
        if j == letter:
            total +=1
    if total >= lower and total <=upper:
        validPass +=1


print(validPass)
