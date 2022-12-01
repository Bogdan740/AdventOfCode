import numpy as np

f = open("puzzleinput.txt", "r")
testData = f.read()
f.close()

inputArr = list(map(lambda x:list(map(int,x)),testData.split("\n")))
formattedArr = np.array(inputArr)

total = 0

for i,val in enumerate(formattedArr):
  for j,height in enumerate(val):
    neighbours = []
    if(i>0):
      neighbourHeight = formattedArr[(i-1,j)]
      neighbours.append(neighbourHeight > height)
    if(j>0):
      neighbourHeight = formattedArr[(i,j-1)]
      neighbours.append(neighbourHeight > height)
    if(i<formattedArr.shape[0]-1):
      neighbourHeight = formattedArr[(i+1,j)]
      neighbours.append(neighbourHeight > height)
    if(j<formattedArr.shape[1]-1):
      neighbourHeight = formattedArr[(i,j+1)]
      neighbours.append(neighbourHeight > height)
    if(all(neighbours)):
      total+=height+1
print(total)

    