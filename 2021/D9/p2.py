import numpy as np

f = open("puzzleinput.txt", "r")
testData = f.read()
f.close()

inputArr = list(map(lambda x:list(map(int,x)),testData.split("\n")))
formattedArr = np.array(inputArr)

basins = []

def floodfill(positionsToCheck, currentArr):
  print("Current arr : ", currentArr)
  print("positionsToCheck: ", positionsToCheck)

  pos = positionsToCheck.pop(0)
  i,j = pos
  height = formattedArr[pos]
  hasBiggerNeighbours = False
  if(i>0):
    neighbourPos = (i-1,j)
    neighbourHeight = formattedArr[neighbourPos]
    if(neighbourHeight>height):
      hasBiggerNeighbours = True
      positionsToCheck.append(neighbourPos)
  if(j>0):
    neighbourPos = (i,j-1)
    neighbourHeight = formattedArr[neighbourPos]
    if(neighbourHeight>height):
      hasBiggerNeighbours = True
      positionsToCheck.append(neighbourPos)
  if(i<formattedArr.shape[0]-1):
    neighbourPos = (i+1,j)
    neighbourHeight = formattedArr[neighbourPos]
    if(neighbourHeight>height):
      hasBiggerNeighbours = True
      positionsToCheck.append(neighbourPos)
  if(j<formattedArr.shape[1]-1):
    neighbourPos = (i,j+1)
    neighbourHeight = formattedArr[neighbourPos]
    if(neighbourHeight>height):
      hasBiggerNeighbours = True
      positionsToCheck.append(neighbourPos)
  if(hasBiggerNeighbours and not pos in currentArr):
    currentArr.append(pos)
  if len(positionsToCheck) == 0:
    return currentArr
  return floodfill(positionsToCheck, currentArr)

print(floodfill([(0,0)],[]))

    