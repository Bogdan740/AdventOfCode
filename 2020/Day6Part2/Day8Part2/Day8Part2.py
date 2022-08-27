file = open("day8input.txt","r")
x = file.read()
crudelist = x.split("\n")

actions = []
values = []

for i in crudelist:
    helper = i.split(" ")
    actions.append(helper[0])
    values.append(int(helper[1]))


def iterate(acs):
    pointer = 0
    acc = 0
    actionsdone = []
    theone = False
    while True:
        try:
            helper = acs[pointer]
        except IndexError:
            theone = True
            break
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
    if theone == True:
        return acc
    else:
        pass



pass1 = [i for i, x in enumerate(actions) if x == "nop"]
pass2 = [i for i, x in enumerate(actions) if x == "jmp"]


for i in pass1:
    helper = actions.copy()
    helper[i] = "jmp"
    if type(iterate(helper)) == int:
            print(iterate(helper))
for i in pass2:
    helper = actions.copy()
    helper[i] = "nop"
    if type(iterate(helper)) == int:
            print(iterate(helper))


            
            

    
       
