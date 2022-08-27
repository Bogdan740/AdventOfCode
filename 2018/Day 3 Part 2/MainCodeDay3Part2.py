cinput = open("CodeInputDay3Part2.txt", "r")
x = cinput.read()
inputList = x.split("\n")
cinput.close()

def modifylist(lst):
        lst = [elt.strip() if type(elt) is str else elt for elt in lst] #This simply converts every element of a list into an intiger
        while '' in lst:
                lst.remove('')
        return lst
        


        

grid = []
grid2 = []

for i in range(1000):
    grid2.append([0]*1000)

pos1 = []
area= []
pos = []
coordx = []
coordy = []
width = []
height = []

for i in inputList:
    x = i.split()
    pos1.append(x[2])
    area.append(x[3])
for i in pos1:
    x = i.replace(":","")
    pos.append(x)
for i in pos:
    x = i.split(",")
    coordx.append(x[0])
    coordy.append(x[1])
for i in area:
    x = i.split("x")
    width.append(x[0])
    height.append(x[1])

coordy = list(map(int,coordy))
coordx = list(map(int,coordx))

coordy = modifylist(coordy)
coordx = modifylist(coordx)

for i in range(len(inputList)):
    smm = height[i]
    smm = int(smm)
    smm1 = width[i]
    smm1 = int(smm1)
    smm2 = int(coordy[i])
    smm3 = int(coordx[i])
    for x in range(smm):
            for z in range(smm1):
                    grid2[smm2 + x][smm3 + z] +=1



for i in range(len(inputList)):
        tester = 0
        smm = int(height[i])
        smm1 = int(width[i])
        smm2 = int(coordy[i])
        smm3 = int(coordx[i])
        for x in range(smm):
                for z in range(smm1):
                        if (grid2[smm2+x][smm3+z]) == 1:
                                tester +=1
                if tester == (smm * smm1) and tester > 0:
                                print(inputList[i])
                              
                        
                        
                        
                        
  #Code By Bogdan Cuciureanu  # NOTE when using this code don't forget to use your own input
 #Any suggestions on how to make it better will not be ignored, feel free to submit your code :)
                                
                









                    

