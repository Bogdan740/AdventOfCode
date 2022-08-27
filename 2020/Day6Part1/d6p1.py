file = open("d6input.txt","r")
x = file.read()
crudelist = x.split("\n")

tempList = []
groups = []

for i in crudelist:
    if i != "":
        tempList.append(i)
    else:
        groups.append(tempList)
        tempList = []
        
groups.pop()

questionsAns = []

for i in groups:
    questions = list('abcdefghijklmnopqrstuvwxyz')
    for j in i:
        helper = list(j)
        for k in helper:
            if k in questions:
                questions.remove(k)
            else:
                pass
    questionsAns.append(int(26-len(questions)))
print(sum(questionsAns))
