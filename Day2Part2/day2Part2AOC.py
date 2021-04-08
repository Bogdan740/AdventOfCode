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
    if passChecker[lower] == letter:
        checker1 = "t"
    else:
        checker1 = "f"
    if passChecker[upper] == letter:
        checker2 = "t"
    else:
        checker2 = "f"
    if checker1 == "f" and checker2 == "t":
        validPass +=1
    if checker1 == "t" and checker2 == "f":
        validPass +=1
        


print(validPass)
