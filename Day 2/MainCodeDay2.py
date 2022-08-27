import time

cinput = open("CodeInputDay2.txt", "r")
x = cinput.read()
inputList = x.split("\n")
cinput.close()


def checkSum(x):
    a = list(x)
    return a



alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

rep3 = 0
rep2 = 0


for i in range(0,len(inputList)):
    smm = checkSum(inputList[i])
    check1 = 0
    check2 = 0
    
    for i in range(0,26):
        counter = smm.count(alphabet[i])
        if counter == 2 and check1 < 1:
            rep2 +=1
            check1 +=1
        else:
            pass
        if counter == 3 and check2 < 1:
            rep3 +=1
            check2 +=1
        else:
            pass
 

print("TWO CAME UP : ",rep2," TIMES")
print("THREE CAME UP : ",rep3," TIMES")
print("")
finalValue = rep2 * rep3
print("TOTAL = ",finalValue)

#Code By Bogdan Cuciureanu  # NOTE when using this code don't forget to use your own input
#Any suggestions on how to make it better will not be ignored, feel free to submit your code :)



        
