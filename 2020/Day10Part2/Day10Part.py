import random
import time


def cls():
    print(" \n"*5)

file = open("day10input.txt","r")
x = file.read()
crudelist = x.split("\n")

for i in range(len(crudelist)):
    crudelist[i] = int(crudelist[i])
cls()

crudelist.append(0)
crudelist.append(max(crudelist)+3)
crudelist = sorted(crudelist)

pathways = {}

def findNumbWays(pointer):
    if pointer == len(crudelist)-1:
        return 1
    if pointer in pathways:
        return pathways[pointer]

    total = 0

    for i in range(pointer+1,len(crudelist)):
        if crudelist[i] - crudelist[pointer] <= 3:
            total += findNumbWays(i)
    
    
    pathways[pointer] = total
    
    return total

print(findNumbWays(0))

