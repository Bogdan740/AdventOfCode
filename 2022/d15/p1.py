f = open("input.txt", "r")

inp = [[tuple(map(int,pair.split(","))) for pair in line.split(" -> ")] for line in f.read().split("\n")]

minX = min(map(min,[[pair[0] for pair in line] for line in inp]))
maxX = max(map(max,[[pair[0] for pair in line] for line in inp]))
maxY = max(map(max,[[pair[1] for pair in line] for line in inp]))

grid = [ ["." for _ in range(minX,maxX+1)] for _ in range(maxY+1)]

# Transform the coordinates so that they fit on our new grid

rocks = [ [ (x-minX,y) for x,y in line] for line in inp]
sand = 500-minX # x-loc of sand source


for rock in rocks:
  for i in range(len(rock)-1):
    x1,y1= rock[i]
    x2,y2= rock[i+1]
    if(x1 == x2):
      may = max(y1,y2)
      miy= min(y1,y2)
      for j in range(miy,may+1):
        grid[j][x2] = "#"
    elif(y1 == y2):
      mx = max(x1,x2)
      mix= min(x1,x2)
      for j in range(mix,mx+1):
        grid[y1][j] = "#"
  
sandFallingOff = False
sandCounter = 0
# Simulate the sand
while(not sandFallingOff):
  x,y = sand, 0
  while(True):
    #Drop the sand particle down as fasr as you can
    below = grid[y+1][x]
    if(below == '.'):
      x,y = x,y+1
      continue
    #Try down and to the left
    if(x-1 < 0):
      sandFallingOff = True
      break
    downAndLeft = grid[y+1][x-1]
    if(downAndLeft == '.'):
      x,y = x-1,y+1
      continue
    #Try down and to the right
    if(x+1 >= len(grid[0])):
      sandFallingOff = True
      break
    downAndRight = grid[y+1][x+1]
    if(downAndRight == '.'):
      x,y = x+1,y+1
      continue
    sandCounter+=1
    grid[y][x] = "o"
    break

print(sandCounter)
  
        

