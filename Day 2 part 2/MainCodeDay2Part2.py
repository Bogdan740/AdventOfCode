import time

cinput = open("CodeInputDay2Part2.txt", "r")
x = cinput.read()
inputList = x.split("\n")
cinput.close()


def checkSum(x):
    a = list(x)
    return a
def checkList(x,y):
    check1 = False
    for i in range(0,25):
        if x[i] == y[i]:
            check1 +=1
        else:
            pass
    if check1 == 24:
        return True
    else:
        return False
x = 0
for i in inputList:
    smm = checkSum(i)
    for i in range(0,len(inputList)):
        smm1 = checkSum(inputList[i])
        checker = checkList(smm,smm1)
        if checker == True:
            print(x)
            print(smm)
            print(smm1)
            x+=1
            break
        else:
            pass
        
#Code By Bogdan Cuciureanu  # NOTE when using this code don't forget to use your own input
#Any suggestions on how to make it better will not be ignored, feel free to submit your code :)
