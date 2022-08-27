file = open("d6input.txt","r")
x = file.read()
crudelist = x.split("\n")

tempList = []
groups = []
groupLens = []

for i in crudelist:
    if i != "":
        tempList.append(i)
    else:
        groups.append("".join(tempList))
        groupLens.append(len(tempList))
        tempList = []
        
groups.pop()

questionsAns = []

for i,group in enumerate(groups):
    questions = list('abcdefghijklmnopqrstuvwxyz')
    answers = 0
    for question in questions:
        if group.count(question) == groupLens[i]:
            answers +=1
        else:
            pass
    questionsAns.append(answers)
print(sum(questionsAns))
            
        
            
            

