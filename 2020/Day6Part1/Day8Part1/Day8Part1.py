file = open("testinput.txt","r")
x = file.read()
crudelist = x.split("\n")

actions = []
values = []

for i in crudelist:
    helper = i.split(" ")
    actions.append(helper[0])
    values.append(int(helper[1]))

pointer = 0
acc = 0

actionsdone = []

while True:
    helper = actions[pointer]
    if helper == "nop":
        if ("nop",values[pointer],pointer) not in actionsdone:
            actionsdone.append(("nop",values[pointer],pointer))
            pointer += 1
        else:
            #print(helper)
            break
    elif helper == "jmp":
        if ("jmp",values[pointer],pointer) not in actionsdone:
            actionsdone.append(("jmp",values[pointer],pointer))
            pointer += values[pointer]
        else:
            #print(helper)
            break
    elif helper == "acc":
        if ("acc",values[pointer],pointer) not in actionsdone:
            actionsdone.append(("acc",values[pointer],pointer))
            acc += values[pointer]
            pointer +=1
        else:
            #print(helper)
            break
    else:
        pass


print(acc)
    





            
            

    
       
